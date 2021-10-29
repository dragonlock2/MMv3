import time
from adafruit_onewire.bus import OneWireBus

# not the most efficient implementation, but it works
class DS28E05():
	def __init__(self, pin):
		self.ow = OneWireBus(pin)
		self.devices = self.ow.scan()

	def read(self, idx, address, length):
		data = bytearray(length)
		self._select_rom(idx)
		self.ow._writebyte(0xF0)
		self.ow._writebyte(address & 0xFF)
		self.ow._writebyte(0x00)
		self.ow.readinto(data)
		return data

	def write(self, idx, address, data):
		if len(data) <= 0 or address < 0 or address + len(data) > 112:
			return False
		if address % 2 == 1:
			b0 = self.read(idx, address-1, 1)[0]
			self._write_page(idx, address-1, b0, data[0])
			address += 1
			data = data[1:]
		for i in range(0,len(data)-1,2):
			self._write_page(idx, address+i, data[i], data[i+1])
		if len(data) % 2 == 1:
			b1 = self.read(idx, address+len(data), 1)[0]
			self._write_page(idx, address+len(data)-1, data[-1], b1)
		return True

	def _select_rom(self, idx):
		self.ow.reset()
		self.ow._writebyte(0x55) # MATCH_ROM
		self.ow.write(self.devices[idx].rom)

	def _write_page(self, idx, addr, b0, b1):
		self._select_rom(idx)
		self.ow._writebyte(0x55)
		self.ow._writebyte(addr & 0x7E)
		self.ow._writebyte(0xFF)
		self.ow._writebyte(b0)
		self.ow._writebyte(b1)
		if self.ow._readbyte() != b0 or self.ow._readbyte() != b1:
			raise Exception("data readback mismatch!")
		self.ow._writebyte(0xFF)
		time.sleep(0.016)
		if self.ow._readbyte() != 0xAA:
			raise Exception("write fail!")
