import machine
import time

class IRSensor():
	def __init__(self, en, a, b, adc):
		self.en  = machine.Pin(en, machine.Pin.OUT)
		self.a   = machine.Pin(a,  machine.Pin.OPEN_DRAIN)
		self.b   = machine.Pin(b,  machine.Pin.OPEN_DRAIN)
		self.adc = machine.ADC(adc)

		self.en(0)
		self.a(1)
		self.b(1)

	def read(self):
		self.en(1)
		self.a(0)
		time.sleep(0.001)
		a = self.adc.read_u16()
		self.a(1)
		self.b(0)
		time.sleep(0.001)
		b = self.adc.read_u16()
		self.b(1)
		self.en(0)
		return (a, b)