from src import microdot as md
import time
from machine import Pin

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
	
	
	
blink_flash(1)
app.run(port=80)
