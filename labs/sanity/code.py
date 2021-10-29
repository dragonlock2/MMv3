import board
import time
import supervisor

import digitalio
import neopixel
import rotaryio

from ds28e05  import DS28E05
from irsensor import IRSensors
from motor    import Motor

supervisor.disable_autoreload()

""" Peripherals """

# debug
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

but = digitalio.DigitalInOut(board.GP3)
but.pull = digitalio.Pull.UP

rgb = neopixel.NeoPixel(board.GP4, 1)

# extra stuffs
eeprom = DS28E05(board.GP2)

# IR sensors
ir = IRSensors(
	board.GP7,  board.GP5,  board.GP6,  board.GP28, # left
	board.GP9,  board.GP10, board.GP11, board.GP26, # center
	board.GP21, board.GP20, board.GP22, board.GP27  # right
)

# encoders
lenc = rotaryio.IncrementalEncoder(board.GP12, board.GP13)
renc = rotaryio.IncrementalEncoder(board.GP19, board.GP18)

# motors
lmot = Motor(board.GP16, board.GP17)
rmot = Motor(board.GP15, board.GP14)

""" Main """

if __name__ == "__main__":
	# debug
	print("Hello World! Press button to begin tests.")
	while (but.value):
		pass

	print("Blinking the LED underneath your micromouse...")
	for _ in range(6):
		led.value = not led.value
		time.sleep(0.25)

	print("Turning on Neopixel on top of your micromouse...")
	rgb[0] = (255, 0, 0)
	time.sleep(0.5)
	rgb[0] = (0, 255, 0)
	time.sleep(0.5)
	rgb[0] = (0, 0, 255)
	time.sleep(0.5)
	rgb[0] = (1, 1, 1)

	# extra stuffs
	if eeprom.devices:
		print("Detected the following 1-Wire devices...")
		for d in eeprom.devices:
			print("\t", "".join("{:02x}".format(x) for x in d.rom))
	else:
		print("FAIL! No 1-Wire devices detected!")

	# IR sensors
	print("Scanning IR sensors! Press button to start and stop.")
	while (but.value):
		pass
	time.sleep(0.05)
	while (not but.value):
		pass

	while (but.value):
		ir.scan()
		print("lir_a:", ir.lir_a, "\t", "lir_b:", ir.lir_b, "\t",
				"cir_a:", ir.cir_a, "\t", "cir_b:", ir.cir_b, "\t",
				"rir_a:", ir.rir_a, "\t", "rir_b:", ir.rir_b
		)
		time.sleep(0.05)
	time.sleep(0.05)
	while (not but.value):
		pass

	# encoders
	print("Reading encoders! Press button to start and stop.")
	while (but.value):
		pass
	time.sleep(0.05)
	while (not but.value):
		pass

	while (but.value):
		print("lenc:", lenc.position, "\t", "renc:", renc.position)
		time.sleep(0.05)
	time.sleep(0.05)
	while (not but.value):
		pass

	# motors
	print("Testing motors! Plug in battery and turn on switch. Press button to start.")
	while (but.value):
		pass

	print("Full speed forward")
	lmot.write(65535)
	rmot.write(65535)
	time.sleep(0.5)
	print("Brake")
	lmot.write(0)
	rmot.write(0)
	time.sleep(0.5)
	print("Full speed backward")
	lmot.write(-65535)
	rmot.write(-65535)
	time.sleep(0.5)
	print("Brake")
	lmot.write(0)
	rmot.write(0)
	time.sleep(0.5)
	print("Low speed forward")
	lmot.write(10000)
	rmot.write(10000)
	time.sleep(0.5)
	print("Brake")
	lmot.write(0)
	rmot.write(0)
	time.sleep(0.5)
	print("Low speed backward")
	lmot.write(-10000)
	rmot.write(-10000)
	time.sleep(0.5)
	print("Brake")
	lmot.write(0)
	rmot.write(0)
	time.sleep(0.5)

	print("Done with tests!")

	print("Just gonna drive straight now :P")
	while True:
		delta = lenc.position - renc.position
		u = 30*delta
		lmot.write(10000-u)
		rmot.write(10000+u)
		print(delta)
		time.sleep(0.05)
