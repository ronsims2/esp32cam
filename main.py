from src import microdot as md
import utime
from machine import Pin
# import camera
# from binascii import b2a_base64

#cam_stat = camera.init(0, format=camera.JPEG)
led_flash = Pin(4, Pin.OUT)
app = md.Microdot()



def blink_flash(t=0):
	led_flash.value(0)
	led_flash.value(1)
	utime.sleep(t)
	led_flash.value(0)
	
	
@app.route('/')
def index(req):
	blink_flash(1)
	
	return 'hello world'
	
	
@app.route('/test')
def test(req):
	return 'testing 1,2,3'


# @app.route('/pic')
# def snap(req):
	# blink_flash(1)
	
	# if cam_stat:
		# pic = camera.capture()
		# return b2a_base64(pic).decode('ascii')
	# else:
		# return 'camera failed to init.'
	
	
blink_flash(0.1)
print('starting server...')
app.run(port=8080)
