import serial
import time

__version__ = '0.2'

class pyDMXController:
    def __init__(self, port, device_type='ftdi'):
        self.port = port
        self.device_type = device_type
        if device_type == 'enttec':
            self.baudrate = 57600
        else:  # default to FTDI settings
            self.baudrate = 250000
        self.serial = serial.Serial(port=self.port, baudrate=self.baudrate, bytesize=8, stopbits=2, parity=serial.PARITY_NONE)
        self.channels = [0] * 512

    def update_channel(self, channel, value):
        if 0 <= channel < 512:
            self.channels[channel] = value

    def send_dmx(self):
        if self.device_type == 'enttec':
            self.send_dmx_enttec()
        else:
            self.send_dmx_ftdi()

    def send_dmx_ftdi(self):
        # FTDI specific DMX protocol
        self.serial.break_condition = True
        time.sleep(0.0000001)
        self.serial.break_condition = False
        time.sleep(0.0000001)
        data = bytearray(self.channels)
        self.serial.write(data)

    def send_dmx_enttec(self):
        # Enttec specific DMX protocol
        msg = bytearray([0x7E, 6])
        data_length = len(self.channels) + 1
        msg.extend(data_length.to_bytes(2, byteorder='little'))
        msg.append(0)  # DMX start code
        msg.extend(bytearray(self.channels))
        msg.append(0xE7)
        self.serial.write(msg)

    def run(self, duration=5):
        start_time = time.time()
        while time.time() - start_time < duration:
            self.send_dmx()
            time.sleep(0.05)

    def close(self):
        self.serial.close()
