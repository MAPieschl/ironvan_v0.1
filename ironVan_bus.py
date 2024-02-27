from smbus2 import SMBus, i2c_msg

import ironVan_log as log

class Bus:
	def __init__(self):
		# Initialize bus from location -1 on RPi
		self.bus = SMBus(1)

		# Stores {device address}: type
		self.devices = {};
		
		for addr in range(0x08, 0x09):
			try:
				# Request device type from address (addr)

				# ???  Update to block data to accept 14 characters  ???
				msg = i2c_msg.read(addr, 1)

				print(msg)

				deviceType = self.bus.i2c_rdwr(msg)

				print(deviceType)

				# ???  Fix dictionary syntax ???
				self.devices[addr] = deviceType

				print(self.devices)
				
			except:
				continue	
				
	def sendCommandCLI(self):
		while(True):
			addr = int(input("Address: "))
			cmd = int(input("Command: "))
			self.bus.write_byte_data(addr, 0, cmd)

	def sendCommand(self, deviceType: str, cmd):
		# Search self.devices for a device that contains the deviceType keyword. Valid keywords include:
		#	- util - utilities device (1 per bus)
		#	- ltsy - lighting system device (1 per bus)
		#	- temp - thermostat device (1 per bus)

		return