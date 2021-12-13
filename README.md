# MMv3

MMv3 is the 3rd generation robot platform used to teach the IEEE Micromouse DeCal at UC Berkeley. It was designed with usability, manufacturability, size, and cost in mind.

## Setup

1. Follow the assembly instructions in [lab1](docs/lab1.md) using the latest **BOM** (see releases).
2. Plug mouse into your computer and upload the latest **firmware.uf2** (see releases) by dragging the file into the `RPI-RP2` folder that shows up. It should disappear and reappear as a `CIRCUITPY` folder.
    * If you've uploaded firmware before, you'll need to hold the `BOOTSEL` button on the Pi Pico while plugging in.
3. Download the latest CircuitPython [libraries](https://circuitpython.org/libraries) (for Version 7.x) and upload the following ones to the lib/ folder on your mouse.
    * adafruit_motor/
    * adafruit_onewire/
    * neopixel.mpy

## Labs

Skeleton lab code, lab documents, and solutions are stored in [labs/](labs/), [docs/](docs/), and [solutions/](solutions/), respectively. To get started with a lab, simply copy the contents of the folder over to the CircuitPython drive and edit files from there.

* [sanity](docs/sanity.md) - Hardware Check
* [lab1](docs/lab1.md) - Assembly and CircuitPython Basics **(WIP)**
* [lab2](docs/lab2.md) - Encoders
* [lab3](docs/lab3.md) - IR Sensors **(WIP)**
* [lab4](docs/lab4.md) - Odometry and Motor Control
* [lab5](docs/lab5.md) - Intro to PID
* [lab6](docs/lab6.md) - More PID **(WIP)**

## Compiling CircuitPython

The DS28E05 1-Wire EEPROM operates at overdrive speeds only. Adding support involves compiling a patched version of CircuitPython.

1. Follow these [instructions](https://learn.adafruit.com/building-circuitpython/introduction) to get your system set up for compilation.
2. Follow these [instructions](https://learn.adafruit.com/building-circuitpython/build-circuitpython) to clone CircuitPython and do further setup but don't compile CircuitPython just yet.
3. Apply [circuitpython.patch](circuitpython.patch) using `patch -p1 < circuitpython.patch`
    * Also apply [macos.patch](macos.patch) if using MacOS.
4. Compile CircuitPython with `cd ports/raspberrypi && make  BOARD=raspberry_pi_pico`
5. Upload the resulting firmware.uf2!
