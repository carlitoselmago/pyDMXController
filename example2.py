from pyDMXController import pyDMXController
dmx = pyDMXController(port='/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_A50285BI-if00-port0', device_type='ftdi')

#fade speed test

dmx.update_channel(6, 255)  # Set channel 6 to maximum

interval=0.00000001

for i in range(255):
    dmx.update_channel(7, i)
    dmx.run(interval)  

dmx.close()