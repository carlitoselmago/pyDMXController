# pyDMXController
A simple DMX python controller for both Enttec USB PRO and the cheap FTDI FT232R controllers

Adapt the port route to your setup

## For Enttec DMX USB Pro
```
dmx = pyDMXController(port='/dev/ttyUSB0', device_type='enttec')
```

## For FTDI FT232R
```
dmx = pyDMXController(port='/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_A50285BI-if00-port0', device_type='ftdi')
```

Tested only on FT232 on Ubuntu, should work on SBCs such as Raspberry pi

Check the example.py for more info on how to use it