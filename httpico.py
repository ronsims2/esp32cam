import usocket
import network
import utime
from machine import Pin
import camera
from binascii import b2a_base64


utime.sleep(10)
cam_stat = camera.init(0, format=camera.JPEG)
utime.sleep(4)

OK_HEADER = 'HTTP/1.0 200 OK\n\n'
ERROR_HEADER = 'HTTP/1.0 500 ERROR\n\n'


def get_httpico(address, port, timeout):

    s = usocket.socket()
    s.setsockopt(usocket.SOL_SOCKET, usocket.SO_REUSEADDR, 1)
    s.settimeout(timeout)
    s.bind((address, port))
    s.listen(1)
    
    
    _httpico = {
        'address': address,
        'port': port,
        'socket': s
    }
    
    return _httpico


def start_server(_httpico, callback):
    if _httpico is None:
        return False
        
    while True:
        client_conn, client_addr = _httpico['socket'].accept()
        req = client_conn.recv(1024).decode()
        
        print(req)
        
        if callback is None:
            resp = ERROR_HEADER + 'No route handler specified.'
        else:
            filtered = callback(req)
            client_conn.sendall(filtered)
            client_conn.close()
        


def httpico_callback(req):
    if cam_stat:
        # This flip does some weird striping me no like
        # camera.flip(1) 
        pic = camera.capture()
        # camera.deinit()
        return OK_HEADER + b2a_base64(pic).decode('ascii')
    else:
        return ERROR_HEADER + 'Cam error, cam status: {}'.format(cam_stat)



wlan = network.WLAN(network.STA_IF)
info = wlan.ifconfig()
print(info)
h = get_httpico(info[0], 8080, 360)
start_server(h, httpico_callback)

led_flash = Pin(4, Pin.OUT)
led_flash.value(1)
utime.sleep(0.1)
led_flash.value(0)
