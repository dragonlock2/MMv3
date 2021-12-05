# Lab 3: IR Sensors

## Background (WIP)

IR sensors work by sending out IR light and measuring the amount reflected back. They take a lot more work to calibrate and are surface dependent, but are far cheaper and faster than the ToF sensors we used to use. Our mouse has 6 of these sensors split into 3 pairs (front, left, right). Having 2 sensors per side allows us to statically determine both the distance and angle of the nearest surface.

IR sensors consist of both an IR emitter and detector. IR emitters draw around 50mA each when on so we have a switch to turn them off when not needed. IR detectors shift their IV curve based on light intensity. To convert that to a readable voltage signal, we'll use a setup similar to a resistor divider. It's less accurate but uses way fewer parts.

TODO check that a reverse bias detector actually works better in terms of linearity, tunability, and consistency.

## Read One Sensor (WIP)

### Checkoff #1

## Read All the Sensors (WIP)

### Checkoff #2

## Calibration (WIP)

### Checkoff #3