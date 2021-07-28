from src import microdot as md
import time
from machine import Pin
import camera

led_flash = Pin(4, Pin.OUT)
# cam_stat = cam_up()
app = md.Microdot()


def cam_up():
	attempts = 0
	up = false
	try:
		while attempts < 10 and up is not False:
			up = camera.init(0, format=camera.JPEG)
			attempts += 1
			if up:
				return up
			else:
				camera.deinit()
				time.sleep(1)
	except Exception as e:
		return str(e)



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
	return cam_up()


@app.route('/pic')
def snap(req):
	blink_flash(1)
	# give cam time to focus
	time.sleep(2)
	pic = camera.capture()
	
	return pic
	
	
	
blink_flash(1)
app.run(port=80, debug=True)
