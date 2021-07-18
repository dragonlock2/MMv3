import machine

class Motor():
	def __init__(self, in1, in2):
		self.in1 = machine.PWM(machine.Pin(in1))
		self.in2 = machine.PWM(machine.Pin(in2))

		self.in1.freq(20000)
		self.in2.freq(20000)

		self.write(0)

	def write(self, speed):
		# speed: -65535 to +65535
		if speed >= 0:
			self.in1.duty_u16(65535)
			self.in2.duty_u16(65535-speed)
		else:
			self.in1.duty_u16(65535+speed)
			self.in2.duty_u16(65535)