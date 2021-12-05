# Lab 1: CircuitPython Basics

## Assembly (WIP)

Use the latest `ibom.html`.

## Sanity Check

Now that your mouse is assembled, it is time to run a sanity check to make sure everything is working.

1. Plug your mouse into your computer and upload the latest **firmware.uf2** (see [releases](https://github.com/dragonlock2/MMv3/releases)) by dragging it into the drive named `RPI-RP2` that shows up. It should disappear and reappear as a drive named `CIRCUITPY`.
    * If you've uploaded firmware before, you'll need to hold the `BOOTSEL` button on the Pi Pico while plugging in.
2. Download the latest CircuitPython [libraries](https://circuitpython.org/libraries) (for Version 7.x) and upload the following ones to the lib/ folder on your mouse.
    * adafruit_onewire/
    * neopixel.mpy
3. Follow the [sanity lab](sanity.md) to run the sanity check.

### Checkoff #1

1. Show your mentor your assembled mouse and passing sanity check.

## CircuitPython Basics (WIP)

One of the most convenient features of CircuitPython is the ability to upload and modify code as if they were just files on a flash drive. Instead of editing code directly on the drive, we highly recommend editing code locally on your computer first and then copying it over to the drive to run. This reduces wear on the flash memory and ensures you have a local backup of your code.

On startup, CircuitPython looks for a file named `code.py` and runs it. There are a few differences, but for the most part it behaves just like normal Python. After uploading new code, you might need to bring up a serial monitor and press CTRL-C and CTRL-D to reload.

For debugging, the serial monitor is invaluable. This is where the output of `print` statements will go. You can even bring up a REPL. One important note is that you can't start an interactive session (e.g. `python -i code.py`) to further debug your code as CircuitPython will restart on entering one.

### Example 1: Blinky

Let's start with the blink example, the "Hello World" of embedded programming. Your mouse has a green LED on the Pi Pico and an onboard WS2812B NeoPixel RGB LED. Upload the following code to your mouse.

```python
import board     # pin definitions
import time      # time delay
import neopixel  # to control the WS2812B
import digitalio # to control the LED

print("Hello World!")

# setup the LED as an output
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# setup the WS2812B
rgb = neopixel.NeoPixel(board.GP4, 1)

# blink
while True:
    rgb[0] = (255, 255, 255) # max brightness
    led.value = True
    time.sleep(0.5)
    rgb[0] = (0, 0, 0)
    led.value = False
    time.sleep(0.5)
```

Running the code, both LEDs should start blinking every 0.5s. Notice that before we start writing values to the LEDs, we need to set them up with the correct physical pin. Also, WS2812Bs can be chained into strings which is why we use `rgb[0]`, to address the first (and only) LED.

### Checkoff #2

1. Change something about the provided blink code such as RGB color and blink rate.

### Example 2: Unnecessarily Complex Blinky

Let's take a look at some more syntax. Upload the following code to your mouse.

```python
import board
import time
import neopixel

rgb = neopixel.NeoPixel(board.GP4, 1)

counter = 0
while True:
    counter += 1
    if counter % 5 == 0: # modulus a.k.a remainder
        rgb[0] = (100, 0, 0)
        time.sleep(0.5)
        rgb[0] = (0, 0, 0)
    else:
        for i in range(5): # 0, 1, 2, 3, 4
            time.sleep(0.1)
```

Here we introduce a couple programming constructs that are very common in coding. The `if` statement (pairable with `elif` and `else`) runs the block of code corresponding to the truthiness of what's next to the `if`. The `for` loop sequentially iterates through an object which in this case is `range(5)`.

### Checkoff #3

1. What is the blink pattern? How long is it on and off for?

### Example 3: 

Finally, let's test out the button on your mouse. It's connected to pin `GP3`. Fill in the TODOs below to have your RGB LED change color when the button is pressed.

```python
import board
import time
import neopixel
import digitalio

rgb = neopixel.NeoPixel(board.GP4, 1)

but = digitalio.DigitalInOut("""TODO which pin?""")
but.pull = digitalio.Pull.UP

while True:
    if but.value: # not pressed
        """TODO one color"""
    else: # pressed
        """TODO other color"""
```

### Checkoff #4

1. Demonstrate your working code.
