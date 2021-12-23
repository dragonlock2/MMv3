# Lab 3 Checkoff Solutions

## Checkoff #1

1. Just looking to see if the readings are good and consistent with other mice. If not, they might have trouble later.

```python
import board
import time
import digitalio
from analogio import AnalogIn

l_en  = digitalio.DigitalInOut(board.GP7)
l_en.direction = digitalio.Direction.OUTPUT
l_en.value = False
l_adc = AnalogIn(board.GP28)

l_a   = digitalio.DigitalInOut(board.GP5)
l_a.direction  = digitalio.Direction.OUTPUT
l_a.drive_mode = digitalio.DriveMode.OPEN_DRAIN
l_a.value = True # high Z mode

l_b   = digitalio.DigitalInOut(board.GP6)
l_b.direction  = digitalio.Direction.OUTPUT
l_b.drive_mode = digitalio.DriveMode.OPEN_DRAIN
l_b.value = True # high Z mode

while True:
    l_en.value = True

    l_a.value = False
    time.sleep(0.001)
    print(l_adc.value, end=" ")
    l_a.value = True

    l_b.value = False
    time.sleep(0.001)
    print(l_adc.value)
    l_b.value = True

    l_en.value = False

    time.sleep(0.05)
```

## Checkoff #2

1. Like checkoff #1, don't really care about how well they did but instead how they acquired wealth.

```python
import board
import time

from irsensor import IRSensors

ir = IRSensors(
    board.GP7,  board.GP5,  board.GP6,  board.GP28, # left
    board.GP9,  board.GP10, board.GP11, board.GP26, # center
    board.GP21, board.GP20, board.GP22, board.GP27  # right
)

while True:
    ir.scan()
    print("lir_a:", ir.lir_a, "\t", "lir_b:", ir.lir_b, "\t",
            "cir_a:", ir.cir_a, "\t", "cir_b:", ir.cir_b, "\t",
            "rir_a:", ir.rir_a, "\t", "rir_b:", ir.rir_b)
    time.sleep(0.05)
```

## Checkoff #3

1. Just check that they ran the code and have reasonable looking constants. The slope tends to be the same with a slight difference in offset. Around `a=0.03` and `b=-50` appear to be the average.
2. This involves combining taking the sensor readings from the previous checkpoint and implementing the provided equation. Example solution is in [chk3_code.py](chk3_code.py).
