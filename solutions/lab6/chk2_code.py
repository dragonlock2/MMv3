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

def constrain(val, min_val, max_val):
    return min(max_val, max(val, min_val))

# compute dist and theta
def compute_odometry():
    MM_PER_TICK = pi * WHEEL_DIAMETER / ENCODER_TICKS_PER_REVOLUTION

    left_dist  = lenc.position * MM_PER_TICK
    right_dist = renc.position * MM_PER_TICK

    dist  = (left_dist + right_dist) / 2
    theta = (right_dist - left_dist) / WHEELBASE_DIAMETER

    return dist, theta

# compute correction and error terms for a target theta
e_ang_sum, e_ang_prev = 0, 0
def compute_u_ang(theta, theta_target):
    Kp, Ki, Kd = 0.1, 0.005, 0.01

    global e_ang_sum, e_ang_prev
    e_ang = theta_target - theta

    # update I
    e_ang_sum += e_ang
    e_ang_sum = constrain(e_ang_sum, -20, 20) # windup

    # update D
    e_ang_deriv = e_ang - e_ang_prev
    e_ang_prev  = e_ang

    u_ang = Kp * e_ang + Ki * e_ang_sum + Kd * e_ang_deriv
    return u_ang, e_ang

# compute correction and error terms for a target distance
e_lin_sum, e_lin_prev = 0, 0
def compute_u_lin(dist, dist_target):
    Kp, Ki, Kd = 0.01, 0.0005, 0.005

    global e_lin_sum, e_lin_prev
    e_lin = dist_target - dist

    # update I
    e_lin_sum += e_lin
    e_lin_sum = constrain(e_lin_sum, -100, 100) # windup

    # update D
    e_lin_deriv = e_lin - e_lin_prev
    e_lin_prev  = e_lin

    u_lin= Kp * e_lin + Ki * e_lin_sum + Kd * e_lin_deriv
    u_lin = constrain(u_lin, -0.3, 0.3)
    return u_lin, e_lin

def run_control_loop(theta_target, dist_target):
    dist, theta = compute_odometry()
    u_ang, e_ang = compute_u_ang(theta, theta_target)
    u_lin, e_lin = compute_u_lin(dist, dist_target)
    lmot.throttle = constrain(u_lin - u_ang, -1, 1)
    rmot.throttle = constrain(u_lin + u_ang, -1, 1)
    return e_ang, e_lin

def reset_odometry():
    lenc.position, renc.position = 0, 0

def reset_controls():
    global e_ang_sum, e_ang_prev, e_lin_sum, e_lin_prev
    e_ang_sum, e_ang_prev, e_lin_sum, e_lin_prev = 0, 0, 0, 0

def turn_left():
    reset_odometry()
    while abs(run_control_loop(pi/2, 0)[0]) > 0.05:
        time.sleep(0.02)
    reset_controls()
    lmot.throttle, rmot.throttle = 0, 0

if __name__ == "__main__":
    while True:
        turn_left()
        time.sleep(1)
