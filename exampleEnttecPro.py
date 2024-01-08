from pyDMXController import pyDMXController
dmx = pyDMXController(port='/dev/ttyUSB0', device_type='enttec')

#fade speed test

#dmx.update_channel(6, 255)  # Set channel 6 to maximum

interval=0.00001

for i in range(8):
    channel=i+1
    print(channel)
    dmx.update_channel(channel, 255)
    dmx.run(interval)  

dmx.close()