# Lab 2: Encoders

## Background

When we're navigating the maze, we'd like to keep track of a couple things.

* Is it driving straight?
* How far has it driven?
* What direction is it facing?

To answer these questions, we'll use the **quadrature encoder** sensors mounted on the back of your motors. They consist of a spinning magnet and two Hall effect sensors mounted 90° apart. Hall effect sensors measure the presence of magnetic fields. In our case, they output a `True` when closer to a north pole and `False` when closer to a south pole.

<p align="center">
    <figure>
        <img height="300px" src="imgs/quadrature_encoder.gif" />
        <br>
        <figcaption align="center"><b>Hall sensor signal (y-axis) vs. time (x-axis)</b></figcaption>
    </figure>
</p>

## Waveform Viewing

Let's try reading raw values from the encoder. Upload the following code.

```python
import board
import time
import digitalio

# left encoder
a = digitalio.DigitalInOut(board.GP12)
b = digitalio.DigitalInOut(board.GP13)

while True:
    print(int(a.value), int(b.value))
    time.sleep(0.001)
```

Pull up a serial monitor and start spinning the left motor at various speeds. Notice how the values start changing. Can you tell which direction the motor is spinning with just one input?

### Checkoff #1

1. What's the output when the motor is stationary? Is it a certain level? Is it constant?
2. How does the output change when you spin the motor faster?
3. Why do we need two Hall effect sensors per motor?

## Polling

Next let's try tracking the position of the left wheel. We're going to use a technique called polling which involves repeatedly reading a signal to detect changes. Fill in the `leftEncoderRisingEdge` function below.

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
    """TODO increment or decrement position"""

while True:
    a_val = a.value
    if a_val and not a_prev: # rising edge
        leftEncoderRisingEdge()
    a_prev = a_val

    if counter % 1000 == 0:
        print(position)
    counter += 1
```

After uploading the code, pull up a serial monitor and start spinning the motor in both directions. The position should go up and down as you do it!

### Checkoff #2

1. Show your working code.
2. Roughly how many "ticks" correspond to a revolution? How do you think this is computed?
3. What issues might the "polling" method have?
4. Now that we can measure position, how might we measure velocity?
5. What effect does swapping the A and B pins have on how we measure position?

## Interrupts

Polling can be inefficient and even miss edges if the wheel is spinning too quickly. Moreover, constantly having to check a signal takes up a lot of CPU time that could be used for other purposes. While polling is adequate in some cases, for an encoder we need something better.

Interrupts literally interrupt the CPU by making it pause its current task and run some other code before resuming. In our case, we want to trigger an interrupt when a pin has a rising edge. The low-level setup for interrupts usually involves enabling some registers and assigning a function to run. CircuitPython actually abstracts all of this away for us in the `rotaryio` module.

Upload the following code.

```python
import board
import time
import rotaryio

enc = rotaryio.IncrementalEncoder(board.GP12, board.GP13)

while True:
    print(enc.position)
    time.sleep(0.001)
```

Pull up a serial monitor and start spinning the motor.

### Checkoff #3

1. Demonstrate the working code.
2. Why might we use interrupts over polling?
