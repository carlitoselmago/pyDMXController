from pyDMXController import pyDMXController
dmx = pyDMXController(port='/dev/ttyUSB0', device_type='enttec')

#fade speed test

dmx.update_channel(1, 255)  # Set channel 6 to maximum

interval=0.0001

for i in range(255):
    dmx.update_channel(2, i)
    dmx.update_channel(3, i)
    dmx.update_channel(4, i)
    dmx.run(interval)  

dmx.close()