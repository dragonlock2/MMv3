import machine

class Encoder():
	def __init__(self, a, b):
		self.a = machine.Pin(a, machine.Pin.IN)
		self.b = machine.Pin(b, machine.Pin.IN)

		self.count = 0

		# X1 encoding (higher needs better encoders)
		self.a.irq(trigger=machine.Pin.IRQ_RISING, handler=self.a_rising)

	def a_rising(self, _):
		self.count += 1 if self.b() else -1

	def read(self):
		return self.count