import board
import ulab.numpy as np

from irsensor import IRSensors

""" Peripherals """

# IR sensors
ir = IRSensors(
    board.GP7,  board.GP5,  board.GP6,  board.GP28, # left
    board.GP9,  board.GP10, board.GP11, board.GP26, # center
    board.GP21, board.GP20, board.GP22, board.GP27  # right
)

""" Main """

MAX_DIST = 60 # mm
STEP = 10 # mm

def lstsq(A, b):
    At = A.transpose()
    return np.dot(np.dot(np.linalg.inv(np.dot(At, A)), At), b)

def calibrate(a, b):
    x_a, d_a, x_b, d_b = [], [], [], []
    for d in np.arange(0, MAX_DIST+1e-3, STEP):
        print("Place wall at", d, "\bmm and press <enter> to record", end="")
        input()
        ir.scan()
        d_a.append(d); d_b.append(d)
        x_a.append(getattr(ir, a)); x_b.append(getattr(ir, b))

    A_a = np.concatenate((
        np.array(x_a).reshape((len(x_a),1)),
        np.ones(len(x_a)).reshape((len(x_a),1))
    ), axis=1)
    d_a = np.array(d_a)

    A_b = np.concatenate((
        np.array(x_b).reshape((len(x_b),1)),
        np.ones(len(x_b)).reshape((len(x_b),1))
    ), axis=1)
    d_b = np.array(d_b)

    return lstsq(A_a, d_a), lstsq(A_b, d_b)

if __name__ == "__main__":
    print("Calibrating left sensors...")
    k_a, k_b = calibrate("lir_a", "lir_b")
    print()
    print("lir_a constants:", "a =", k_a[0], "\tb =", k_a[1])
    print("lir_b constants:", "a =", k_b[0], "\tb =", k_b[1])
    print()

    print("Calibrating center sensors...")
    k_a, k_b = calibrate("cir_a", "cir_b")
    print()
    print("cir_a constants:", "a =", k_a[0], "\tb =", k_a[1])
    print("cir_b constants:", "a =", k_b[0], "\tb =", k_b[1])
    print()

    print("Calibrating right sensors...")
    k_a, k_b = calibrate("rir_a", "rir_b")
    print()
    print("rir_a constants:", "a =", k_a[0], "\tb =", k_a[1])
    print("rir_b constants:", "a =", k_b[0], "\tb =", k_b[1])
    print()
