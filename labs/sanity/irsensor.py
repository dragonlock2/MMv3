import time
import digitalio
from analogio import AnalogIn

class IRSensors():
	def __init__(self, 
		l_en, l_a, l_b, l_adc,
		c_en, c_a, c_b, c_adc,
		r_en, r_a, r_b, r_adc
	):
		# Setup IR LED enables
		self.l_en = digitalio.DigitalInOut(l_en)
		self.c_en = digitalio.DigitalInOut(c_en)
		self.r_en = digitalio.DigitalInOut(r_en)
		for p in [self.l_en, self.c_en, self.r_en]:
			p.direction = digitalio.Direction.OUTPUT
			p.value = False

		# Setup ADCs
		self.l_adc = AnalogIn(l_adc)
		self.c_adc = AnalogIn(c_adc)
		self.r_adc = AnalogIn(r_adc)

		# Setup differential pair enables
		self.l_a = digitalio.DigitalInOut(l_a)
		self.l_b = digitalio.DigitalInOut(l_b)
		self.c_a = digitalio.DigitalInOut(c_a)
		self.c_b = digitalio.DigitalInOut(c_b)
		self.r_a = digitalio.DigitalInOut(r_a)
		self.r_b = digitalio.DigitalInOut(r_b)
		for p in [self.l_a, self.l_b, self.c_a, 
					self.c_b, self.r_a, self.r_b]:
			p.direction = digitalio.Direction.OUTPUT
			p.drive_mode = digitalio.DriveMode.OPEN_DRAIN
			p.value = True # High Z mode

		# Preallocate memory for storing values
		self.lir_a, self.lir_b = 0, 0
		self.cir_a, self.cir_b = 0, 0
		self.rir_a, self.rir_b = 0, 0

	def scan(self):
		# Enable IR LEDs
		for p in [self.l_en, self.c_en, self.r_en]:
			p.value = True

		# Read 'a' channels
		for p in [self.l_a, self.c_a, self.r_a]:
			p.value = False
		time.sleep(0.001)
		self.lir_a = self.l_adc.value
		self.cir_a = self.c_adc.value
		self.rir_a = self.r_adc.value
		for p in [self.l_a, self.c_a, self.r_a]:
			p.value = True

		# Read 'b' channels
		for p in [self.l_b, self.c_b, self.r_b]:
			p.value = False
		time.sleep(0.001)
		self.lir_b = self.l_adc.value
		self.cir_b = self.c_adc.value
		self.rir_b = self.r_adc.value
		for p in [self.l_b, self.c_b, self.r_b]:
			p.value = True
		
		# Disable IR LEDs (save power)
		for p in [self.l_en, self.c_en, self.r_en]:
			p.value = False
