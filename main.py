import network
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

try:
	with open('config.txt') as f:
		config = f.readline()

	ssid,pw = config.split(',')
	wlan.connect(ssid,pw)
	
	timeout = 30
	clock = 0
	while wlan.isconnected() == False:
		if clock >= timeout:
			raise Exception('timeout', 'Could not connect')
			break
			

		print('Connecting to ' + ssid + '...') 
		time.sleep(1)
		clock += 1
		

except Exception as e:
	print(e)

print('Connected to ' + ssid)
