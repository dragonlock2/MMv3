import board
import time
from math import pi

import digitalio
import neopixel
import rotaryio
import pwmio
import adafruit_motor.motor as motor

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

def constrain(val, min_val, max_val):
    return min(max_val, max(val, min_val))

# compute dist and theta
def compute_odometry():
    return """TODO"""

# compute correction and error terms for a target theta
def compute_u_ang(theta, theta_target):
    return """TODO"""

# compute correction and error terms for a target distance
def compute_u_lin(dist, dist_target):
    return """TODO"""

def run_control_loop(theta_target, dist_target):
    dist, theta = compute_odometry()
    u_ang, e_ang = compute_u_ang(theta, theta_target)
    u_lin, e_lin = compute_u_lin(dist, dist_target)
    lmot.throttle = constrain(u_lin - u_ang, -1, 1)
    rmot.throttle = constrain(u_lin + u_ang, -1, 1)
    return e_ang, e_lin

if __name__ == "__main__":
    while True:
        e_ang, e_lin = run_control_loop(0, 200)
        print(e_ang, e_lin)
        time.sleep(0.02) # ~50Hz loop
