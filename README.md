# MMv3

MMv3 is the 3rd generation robot platform used to teach the IEEE Micromouse DeCal at UC Berkeley. It was designed with usability, manufacturability, size, and cost in mind.

## Setup

1. TODO add hardware assembly instructions including full BOM
2. TODO add firmware.uf2 link and upload instructions
3. Download the latest CircuitPython [libraries](https://circuitpython.org/libraries) and upload the following ones to the lib/ folder on your micromouse.
	* adafruit_onewire/
	* neopixel.mpy

## Labs

Skeleton lab code, lab documents, and solutions are stored in [labs/](labs/), [docs/](docs/), and [solutions/](solutions/), respectively. To get started with a lab, simply copy the contents of the folder over to the CircuitPython drive and edit files from there.

* [sanity](docs/sanity.md) - hardware check

## Compiling CircuitPython

The DS28E05 1-Wire EEPROM used on the MMv3.1 and before operates at overdrive speeds only. Adding support involves compiling a patched version of CircuitPython.

1. Follow these [instructions](https://learn.adafruit.com/building-circuitpython/introduction) to get your system set up for compilation.
2. Follow these [instructions](https://learn.adafruit.com/building-circuitpython/build-circuitpython) to clone CircuitPython and do further setup but don't compile CircuitPython just yet.
3. Apply [circuitpython.patch](circuitpython.patch) using `patch -p1 < circuitpython.patch`
	* Also apply [macos.patch](macos.patch) if using MacOS.
4. Compile CircuitPython with `cd ports/raspberrypi && make  BOARD=raspberry_pi_pico`
5. Upload the resulting firmware.uf2!

## Known Issues

* circuitpython.patch does not result in perfect timing for the 1-Wire bus (86% accuracy in detecting the EEPROM). Fixing will take fine tuning timings with an oscilloscope. micropython.patch works perfectly as it was developed with an oscilloscope.
* DS28E05 library doesn't work with CircuitPython but did under MicroPython. Likely because bit timings aren't yet perfect.