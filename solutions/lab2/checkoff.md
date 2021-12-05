# Lab 2 Checkoff Solutions

## Checkoff #1

1. Values are constant.
2. It toggles between 0 and 1 faster.
3. To tell direction. Waveform looks the same forward and backward with just one.

## Checkoff #2

1. There's a couple of ways to do it, but here's one.

```python
import board
import digitalio

# left encoder
a = digitalio.DigitalInOut(board.GP12)
b = digitalio.DigitalInOut(board.GP13)

counter = 0
position = 0
a_prev = a.value

def leftEncoderRisingEdge():
    position += 1 if b.value else -1

while True:
    a_val = a.value
    if a_val and not a_prev: # rising edge
        leftEncoderRisingEdge()
    a_prev = a_val

    if counter % 1000 == 0:
        print(position)
    counter += 1
```

2. About 217. Multiply the gearbox ratio by the number of north poles on the motor magnet.
3. Basically can miss edges and takes up too much CPU time.
4. Use a timer to measure time between edges.
5. Just reverses the direction of measurement.

## Checkoff #3

1. Does it go up and down.
2. Interrupts don't miss edges and don't need the CPU constantly reading. There's still a limit on speed bc of interrupt and function overhead.
