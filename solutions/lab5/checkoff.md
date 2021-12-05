# Lab 5 Checkoff Solutions

## Checkoff #1

1. See that the mouse drives straight. Our motors are actually pretty consistent so the difference may not be obvious. The angular error doesn't actually need to go to 0 since we're measuring distance not velocity. It just needs to be stable. Also take a look at their code since this is the first time there's a decent amount of it. Try to encourage them towards clean and readable code. Solution code is in [chk1_code.py](chk1_code.py).
2. Some combination of a target theta minus the actual theta. They could just say theta, but make sure say we can generalize to any desired theta.
3. <img src="https://render.githubusercontent.com/render/math?math=K_p%3D0.5">
4. Too low and it corrects too slowly or not at all. Too high and it might oscillate and go unstable.

## Checkoff #2

1. See that the mouse drives straight and stops after around 20cm. Don't worry too much about extreme precision. Solution code is in [chk2_code.py](chk2_code.py).
2. Some combination of a target distance minus the current distance.
3. <img src="https://render.githubusercontent.com/render/math?math=K_p%3D0.01">
