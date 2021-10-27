import machine
import rp2
import array

# WS2812B code from https://github.com/raspberrypi/pico-micropython-examples/blob/master/pio/pio_ws2812.py
@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1)               .side(0)    [T3 - 1]
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
    jmp("bitloop")          .side(1)    [T2 - 1]
    label("do_zero")
    nop()                   .side(0)    [T2 - 1]
    wrap()

sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=machine.Pin(4))
sm.active(1)
ar = array.array("I", [0])

def led_rgb(r, g, b):
    ar[0] = (g << 16) + (r << 8) + b
    sm.put(ar, 8)