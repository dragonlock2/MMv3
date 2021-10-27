import machine
import time
import onewire

from neopixel import led_rgb
from irsensor import IRSensor
from encoder  import Encoder
from motor    import Motor
from ds28e05  import DS28E05

""" Pins """

# debug
led = machine.Pin(25, machine.Pin.OUT, value=1)
but = machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_UP)
led_rgb(1, 1, 1)

# extra stuffs
eeprom = DS28E05(2)

# IR sensors
lir = IRSensor(7, 5, 6, 28)
cir = IRSensor(9, 10, 11, 26)
rir = IRSensor(21, 20, 22, 27)

# encoders
lenc = Encoder(12, 13, invert=True)
renc = Encoder(18, 19)

# motors
lmot = Motor(16, 17)
rmot = Motor(14, 15, invert=True)

""" Main """

# while True:
# 	delta = lenc.read() - renc.read()
# 	u = 30*delta
# 	lmot.write(10000-u)
# 	rmot.write(10000+u)
# 	print(delta)
# 	time.sleep(0.05)
