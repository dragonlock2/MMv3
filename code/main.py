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
but = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
led_rgb(1, 1, 1)

# extra stuffs
i2c = machine.I2C(1, sda=machine.Pin(2), scl=machine.Pin(3)) # LSM9DS1
eeprom = DS28E05(4)

# IR sensors
lir = IRSensor(8, 6, 7, 28)
cir = IRSensor(13, 12, 14, 26)
rir = IRSensor(11, 10, 9, 27)

# encoders
lenc = Encoder(16, 17)
renc = Encoder(18, 19)

# motors
lmot = Motor(15, 22)
rmot = Motor(21, 20)

""" Main """
machine.Pin(5, machine.Pin.IN) # temp workaround for rev 1
