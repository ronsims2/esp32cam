import time
from machine import Pin
import camera

cam_stat = camera.init(0, format=camera.JPEG)
time.sleep(4)

led_flash = Pin(4, Pin.OUT)
led_flash.value(1)
time.sleep(0.1)
led_flash.value(0)


if cam_stat:
    pic = camera.capture()
    camera.deinit()
    print(pic)
else:
    print('Cam error, cam status: {}'.format(cam_stat))
