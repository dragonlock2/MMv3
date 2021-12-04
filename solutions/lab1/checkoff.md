# Lab 1 Checkoff Solutions

## Checkoff #1

1. Not much to say here just make sure the mouse is working.

## Checkoff #2

1. Legit can be any change we just want them to get started tinkering.

## Checkoff #3

1. On for 0.5s and then off for 2s.

## Checkoff #4

1. There's quite a few possible solutions just make sure the RGB LED changes color when the button is pressed. Here's one solution.

```python
import board
import time
import neopixel
import digitalio

rgb = neopixel.NeoPixel(board.GP4, 1)

but = digitalio.DigitalInOut(board.GP3)
but.pull = digitalio.Pull.UP

while True:
    if but.value: # not pressed
        rgb[0] = (0, 69, 69)
    else: # pressed
        rgb[0] = (69, 0, 69)
```