from src import microdot as md
import time
from machine import Pin

led_flash = Pin(4, Pin.OUT)
app = md.Microdot()

@app.route('/')
def index(req):
	return 'hello world'
	

def blink_flash(t=0):
	led_flash.value(0)
	led_flash.value(1)
	time.sleep(t)
	led_flash.value(0)
	
	
blink_flash(1)
app.run(port=80)
