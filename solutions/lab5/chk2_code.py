import board
import time
import supervisor
from math import pi

import digitalio
import neopixel
import rotaryio
import pwmio
import adafruit_motor.motor as motor

supervisor.disable_autoreload()

""" Constants """

ENCODER_TICKS_PER_REVOLUTION = 217
WHEELBASE_DIAMETER = 78.0 # mm
WHEEL_DIAMETER = 34.0 # mm

""" Peripherals """

# debug
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

but = digitalio.DigitalInOut(board.GP3)
but.pull = digitalio.Pull.UP

rgb = neopixel.NeoPixel(board.GP4, 1)

# encoders
lenc = rotaryio.IncrementalEncoder(board.GP12, board.GP13)
renc = rotaryio.IncrementalEncoder(board.GP19, board.GP18)

# motors
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

""" Main """

def constr_mot(val, min_val, max_val):
    return min(max_val, max(val, min_val))

if __name__ == "__main__":
    MM_PER_TICK = pi * WHEEL_DIAMETER / ENCODER_TICKS_PER_REVOLUTION

    while True:
        left_dist  = lenc.position * MM_PER_TICK
        right_dist = renc.position * MM_PER_TICK

        dist  = (left_dist + right_dist) / 2
        theta = (right_dist - left_dist) / WHEELBASE_DIAMETER

        # angular P control
        Kp_ang = 0.1
        theta_target = 0

        e_ang = theta_target - theta
        u_ang = Kp_ang * e_ang

        # linear P control
        Kp_lin = 0.01
        dist_target = 200

        e_lin = dist_target - dist
        u_lin = constr_mot(Kp_lin * e_lin, -0.3, 0.3) # 0.9 is a bit too fast

        # combine
        lmot.throttle = constr_mot(u_lin - u_ang, -1, 1)
        rmot.throttle = constr_mot(u_lin + u_ang, -1, 1)

        print(e_ang, e_lin)

        time.sleep(0.05)
