# Lab 3: IR Sensors

## Background

IR sensors work by sending out IR light and measuring the amount reflected back. They take a lot more work to calibrate and are surface dependent, but are far cheaper and faster than the ToF sensors we used to use. Our mouse has 6 of these sensors split into 3 pairs (center/front, left, right). Having 2 sensors per side allows us to statically determine both the distance and angle of the nearest surface.

IR sensors consist of both an IR emitter and detector. IR emitters draw around 50mA each when on, so we have a switch to turn them off when not needed. IR detectors shift their IV curve based on light intensity like in the following graph.

<p align="center">
    <img height="250px" src="https://courses.engr.illinois.edu/ece110/sp2021/content/courseNotes/files/images/photodiodes/PhotodiodeIV.png"/>
</p>

To convert that to a readable voltage signal, we'll use a setup similar to a resistor divider. It's noisier and less tunable compared to a transimpedance amplifier, but uses only one resistor. By placing the IR detector in reverse bias, we use the flatter region of the IV curve. Since the current varies linearly with light intensity, the voltage also varies linearly. MMv3 uses the following circuit (pull-up resistor not shown).

<p align="center">
    <img height="200px" src="imgs/ir_circuit.png"/>
</p>

## Read One Sensor

Since we have 6 total analog sensors but only 3 ADC pins on the Pi Pico, we need to multiplex 2 sensors onto each pin. We use one extra pin on each IR detector in open-drain mode to fully disconnect or connect it to ground. To read in one sensor, we perform the following steps.

1. Enable the IR emitters (set pin to `True`).
2. Enable the chosen sensor by connecting it to ground (set pin to `False`).
3. Wait around 1ms for things to settle.
4. Take the reading.
5. Disable the chosen sensor by setting the pin to open-drain (set pin to `True`).
6. Disable the IR emitters (set pin to `False`).

Baesd on the above steps and the `AnalogIn` [documentation](https://circuitpython.readthedocs.io/en/latest/shared-bindings/analogio/index.html), fill out the below TODOs to print out readings from the left IR sensor pair (`lir_a` and `lir_b`).

```python
import board
import time
import digitalio
from analogio import AnalogIn

l_en  = """TODO create DigitalInOut output on GP7"""
l_adc = """TODO create AnalogIn on GP28"""

l_a   = digitalio.DigitalInOut(board.GP5)
l_a.direction  = digitalio.Direction.OUTPUT
l_a.drive_mode = digitalio.DriveMode.OPEN_DRAIN
l_a.value = True # high Z mode

l_b = """TODO create DigitalInOut on GP6 in open-drain mode"""

while True:
    # TODO enable IR emitters using l_en
    # TODO enable chosen sensor l_a or l_b
    # TODO wait a bit
    # TODO take analog reading for future printing
    # TODO disable chosen sensor l_a or l_b
    # TODO disable IR emitters using l_en
    time.sleep(0.05)
```

### Checkoff #1

1. Demonstrate one working sensor.

## Read All the Sensors

In order to simplify the whole process of multiplexing and reading from multiple sensors, we wrote a library. Upload `irsensor.py` from [sanity/](../labs/sanity) to serve as the library. Read through `irsensor.py` to instantiate and use it and fill out the below TODOs to print out all sensor readings in real time.

```python
import board
import time

from irsensor import IRSensors

ir = IRSensors(
    """TODO sensor | en   | a    | b    | adc"""
    """TODO lir    | GP7  | GP5  | GP6  | GP28"""
    """TODO cir    | GP9  | GP10 | GP11 | GP26"""
    """TODO rir    | GP21 | GP20 | GP22 | GP27"""
)

while True:
    """TODO get and print all sensor readings"""
    time.sleep(0.05)
```

### Checkoff #2

1. Demonstrate all of your working sensors.

## Calibration

Let's try estimating actual distances from the sensor values. Empirically, the relationship is linear below around 60mm and rises sharply beyond that due to the angled sensors seeing above the wall. Based on maze cell size, we really only need accurate distances around 50mm for wall following and just binary wall detection beyond that.

<p align="center">
    <img height="250px" src="imgs/ir_graph.png"/>
    <br>
    <a><b>IR Sensor Linear Region</b></a>
</p>

Load up [`code.py`](../labs/lab3/code.py) which contains code to automate finding the constants. You'll be using a maze wall and ruler to take readings at various distances. The code then uses least squares to fit a line to the points and prints out the constants at the end. The equation using these constants to convert sensor readings to distances can be expressed as follows.

<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=distance%3Da%5Ccdot%20sensor%2Bb">
</p>

### Checkoff #3

1. Run the calibration code and save the constants somewhere.
2. Using the constants, write code to convert sensor values to distances.
