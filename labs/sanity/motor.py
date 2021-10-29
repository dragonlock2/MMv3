import pwmio

class Motor():
	def __init__(self, in1, in2):
		self.in1 = pwmio.PWMOut(in1, frequency=20000)
		self.in2 = pwmio.PWMOut(in2, frequency=20000)
		self.write(0)

	def write(self, speed):
		speed = self._constrain(speed, -65535, 65535)
		if speed >= 0:
			self.in1.duty_cycle = 65535
			self.in2.duty_cycle = 65535-speed
		else:
			self.in1.duty_cycle = 65535+speed
			self.in2.duty_cycle = 65535

	def _constrain(self, val, min_val, max_val):
		return min(max_val, max(min_val, val))