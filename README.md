# pyDMXController
A simple DMX python controller for both Enttec USB PRO and the cheap FTDI FT232R controllers

## For Enttec DMX USB Pro
dmx = DMXController(port='/dev/ttyUSB0', device_type='enttec')

## For FTDI FT232R
dmx = DMXController(port='/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_A50285BI-if00-port0', device_type='ftdi')

Tested only on FT232 on Ubuntu, should run on SBCs such as Raspberry pi