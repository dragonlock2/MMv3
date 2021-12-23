import board
import time

from irsensor import IRSensors

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

""" Peripherals """

# IR sensors
ir = IRSensors(
    board.GP7,  board.GP5,  board.GP6,  board.GP28, # left
    board.GP9,  board.GP10, board.GP11, board.GP26, # center
    board.GP21, board.GP20, board.GP22, board.GP27, # right
    avg = 10
)

""" Main """

dist = Distance(ir,
    0.0299, -63.6, 0.0195, -39.1,
    0.0300, -60.4, 0.0251, -47.9,
    0.0258, -50.5, 0.0292, -54.0,
)

if __name__ == "__main__":
    while True:
        dist.scan()
        print("lir_a:", dist.la, "\t", "lir_b:", dist.lb, "\t",
                "cir_a:", dist.ca, "\t", "cir_b:", dist.cb, "\t",
                "rir_a:", dist.ra, "\t", "rir_b:", dist.rb)
        time.sleep(0.05)
