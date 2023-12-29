from pyDMXController import pyDMXController
import time 

# Example of usage
dmx =  pyDMXController(port='/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_A50285BI-if00-port0', device_type='ftdi')

dmx.update_channel(6, 255)  # Set channel 6 to maximum

interval=0.001

for i in range(10):
    dmx.update_channel(8,0) 
    dmx.update_channel(7, 255)  
    dmx.run(interval)  
    dmx.update_channel(7, 0) 
    dmx.update_channel(8, 255) 
    dmx.run(interval)

dmx.update_channel(8, 0) 
dmx.run(interval)

dmx.close()
