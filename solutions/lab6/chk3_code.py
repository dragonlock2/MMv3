import board
import time
from math import pi

import rotaryio
import pwmio
import adafruit_motor.motor as motor

from irsensor import IRSensors

""" Constants """

ENCODER_TICKS_PER_REVOLUTION = 217
WHEELBASE_DIAMETER = 78.0 # mm
WHEEL_DIAMETER = 34.0 # mm

""" Peripherals """

# IR sensors
ir = IRSensors(
    board.GP7,  board.GP5,  board.GP6,  board.GP28, # left
    board.GP9,  board.GP10, board.GP11, board.GP26, # center
    board.GP21, board.GP20, board.GP22, board.GP27, # right
    avg = 10
)

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

""" Extra Code """
class Distance():
    def __init__(self,
        ir,
        la_a, la_b, lb_a, lb_b,
        ca_a, ca_b, cb_a, cb_b,
        ra_a, ra_b, rb_a, rb_b,
    ):
        # store constants
        self.ir = ir
        self.la_a, self.la_b, self.lb_a, self.lb_b = la_a, la_b, lb_a, lb_b
        self.ca_a, self.ca_b, self.cb_a, self.cb_b = ca_a, ca_b, cb_a, cb_b
        self.ra_a, self.ra_b, self.rb_a, self.rb_b = ra_a, ra_b, rb_a, rb_b

        # allocate memory for distances
        self.la, self.lb = 0, 0
        self.ca, self.cb = 0, 0
        self.ra, self.rb = 0, 0

    def scan(self):
        ir.scan()
        self.la = self.la_a * ir.lir_a + self.la_b
        self.lb = self.lb_a * ir.lir_b + self.lb_b
        self.ca = self.ca_a * ir.cir_a + self.ca_b
        self.cb = self.cb_a * ir.cir_b + self.cb_b
        self.ra = self.ra_a * ir.rir_a + self.ra_b
        self.rb = self.rb_a * ir.rir_b + self.rb_b

""" Main """

ir_dist = Distance(ir,
    0.0299, -63.6, 0.0195, -39.1,
    0.0300, -60.4, 0.0251, -47.9,
    0.0258, -50.5, 0.0292, -54.0,
)

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
def compute_u_ang(dist, dist_target):
    Kp_theta = 0.01
    Kp_ang = 0.01

    e_theta = dist_target - dist

    theta_target = Kp_theta * e_theta
    theta = ir_dist.la - ir_dist.lb

    e_ang = theta_target - theta

    u_ang = Kp_ang * e_ang
    u_ang = constrain(u_ang, -0.3, 0.3)

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

def run_control_loop(dist_target):
    dist, theta = compute_odometry()
    ir_dist.scan()
    u_ang, e_ang = compute_u_ang(ir_dist.la, 45)
    u_lin, e_lin = compute_u_lin(dist, dist_target)
    lmot.throttle = constrain(u_lin - u_ang, -1, 1)
    rmot.throttle = constrain(u_lin + u_ang, -1, 1)
    return e_ang, e_lin

def reset_odometry():
    lenc.position, renc.position = 0, 0

def reset_controls():
    global e_ang_sum, e_ang_prev, e_lin_sum, e_lin_prev
    e_ang_sum, e_ang_prev, e_lin_sum, e_lin_prev = 0, 0, 0, 0

def forward():
    reset_odometry()
    while abs(run_control_loop(180)[1]) > 3:
        time.sleep(0.02)
    reset_controls()
    lmot.throttle, rmot.throttle = 0, 0

if __name__ == "__main__":
    while True:
        forward()
        time.sleep(1)
