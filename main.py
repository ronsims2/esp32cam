from src import microdot as md
import time
from machine import Pin
import camera

led_flash = Pin(4, Pin.OUT)
app = md.Microdot()

def init_cam(attempt=10):
	tries = 0
	success = False
	
	while tries < attempt or not success:
		try:
			cam_stat = camera.init(0, format=camera.JPEG)
			camera.framesize(camera.FRAME_240x240)
			if cam_stat:
				success = True
		except Exception as e:
			print(e.message)
		finally:
			tries += 1
			time.sleep(2.5)
			
	return success


def blink_flash(t=0):
	led_flash.value(0)
	led_flash.value(1)
	time.sleep(t)
	led_flash.value(0)
	
	
@app.route('/')
def index(req):
	blink_flash(1)
	
	return 'hello world'
	
	
@app.route('/cam-up')
def test(req):
	return 'Camera up:'


@app.route('/pic')
def snap(req):
	blink_flash(1)
	
	if init_cam():
		pic = camera.capture()
		camera.deinit()
		
		return 'foobar'
	
	
blink_flash(0.1)
app.run(port=8080)
