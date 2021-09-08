import time
from machine import Pin
import camera
from binascii import b2a_base64

cam_stat = camera.init(0, format=camera.JPEG)
time.sleep(4)

led_flash = Pin(4, Pin.OUT)
led_flash.value(1)
time.sleep(0.1)
led_flash.value(0)


if cam_stat:
    # This flip does some weird striping me no like
    # camera.flip(1) 
    pic = camera.capture()
    camera.deinit()
    print(b2a_base64(pic).decode('ascii'))
else:
    print('Cam error, cam status: {}'.format(cam_stat))
