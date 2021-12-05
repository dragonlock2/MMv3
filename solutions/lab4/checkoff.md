# Lab 4 Checkoff Solutions

## Checkoff #1

1. Have them manually move the mouse straight and see if the distance roughly matches. Then have them rotate in place and see if the angle matches.

```python
import board
import time
import rotaryio
from math import pi

lenc = rotaryio.IncrementalEncoder(board.GP12, board.GP13)
renc = rotaryio.IncrementalEncoder(board.GP19, board.GP18)

ENCODER_TICKS_PER_REVOLUTION = 217
WHEELBASE_DIAMETER = 78.0 # mm
WHEEL_DIAMETER = 34.0 # mm

while True:
    MM_PER_TICK = pi * WHEEL_DIAMETER / ENCODER_TICKS_PER_REVOLUTION
    left_dist  = lenc.position * MM_PER_TICK
    right_dist = renc.position * MM_PER_TICK

    dist  = (left_dist + right_dist) / 2
    theta = (right_dist - left_dist) / WHEELBASE_DIAMETER

    print(dist, theta)
    time.sleep(0.05)
```

2. About 0.5mm

## Checkoff #2

1. Just needs to be moving at somewhat low speed. Run the code below to get a feel for it. Don't worry about direction. The biggest gotcha is that the IN2 pin needs to be on 75% of the time instead of 25% to get 25% speed.

```python
import board
import pwmio

lmot_in1 = pwmio.PWMOut(board.GP16, frequency=20000)
lmot_in2 = pwmio.PWMOut(board.GP17, frequency=20000)

while True:
    lmot_in1.duty_cycle = 65535
    lmot_in2.duty_cycle = 49151
```

2. Motor direction will reverse.

## Checkoff #3

1. Make sure it does motions specified in the TODOs.

```python
import board
import time
import pwmio
import adafruit_motor.motor as motor

lmot = motor.DCMotor(
    pwmio.PWMOut(board.GP16, frequency=20000),
    pwmio.PWMOut(board.GP17, frequency=20000)
)
rmot = motor.DCMotor(
    pwmio.PWMOut(board.GP15, frequency=20000),
    pwmio.PWMOut(board.GP14, frequency=20000)
)
lmot.decay_mode = motor.SLOW_DECAY
rmot.decay_mode = motor.SLOW_DECAY

while True:
    lmot.throttle, rmot.throttle = 1, 1
    time.sleep(1)
    lmot.throttle, rmot.throttle = 0, 0
    time.sleep(1)
    lmot.throttle, rmot.throttle = -0.25, -0.25
    time.sleep(1)
    lmot.throttle, rmot.throttle = 0, 0
    time.sleep(1)
```

2. It throws an error. Let them know that means we need to keep values within the valid range for future labs.