from src import microdot as md
import time
from machine import Pin
import camera

led_flash = Pin(4, Pin.OUT)
app = md.Microdot()


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
	cam_stat = camera.init(0, format=camera.JPEG)
	# give cam time to focus
	time.sleep(2)
	pic = camera.capture()
	
	return cam_stat
	
	
	
blink_flash(0.1)
app.run(port=8080)
