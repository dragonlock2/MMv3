import machine
import onewire
import time

# not the most efficient implementation, but it works
class DS28E05():
	def __init__(self, pin):
		self.ow = onewire.OneWire(machine.Pin(pin))
		self.devices = self.ow.scan()

	def read(self, idx, address, length):
		data = bytearray(length)
		self.ow.select_rom(self.devices[idx])
		self.ow.writebyte(0xF0)
		self.ow.writebyte(address & 0xFF)
		self.ow.writebyte(0x00)
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

	def _write_page(self, idx, addr, b0, b1):
		self.ow.select_rom(self.devices[idx])
		self.ow.writebyte(0x55)
		self.ow.writebyte(addr & 0x7E)
		self.ow.writebyte(0xFF)
		self.ow.writebyte(b0)
		self.ow.writebyte(b1)
		if self.ow.readbyte() != b0 or self.ow.readbyte() != b1:
			raise Exception("data readback mismatch!")
		self.ow.writebyte(0xFF)
		time.sleep(0.016)
		if self.ow.readbyte() != 0xAA:
			raise Exception("write fail!")
