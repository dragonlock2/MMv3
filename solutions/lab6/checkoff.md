# Lab 6 Checkoff Solutions

## Checkoff #1

1. Remember Riemann sums from calculus? Basically we just add up the measured error over time. Technically we're supposed to multiply by dt, but that's just a scalar error.
2. Go back to the definition of derivative. Basically we take the difference between our current error and previous error. Technically we're supposed to divide by dt, but that again a scalar error.
3. The main idea is that we limit the size of the integral term. A good limit is whatever value of the integral term causes the maximum power to be put into the motor.

## Checkoff #2

1. As long as it drives straight 200mm and stops like in Lab 5, it's good.
2. As long as it turns in place about 90° and stops, it's good.
3. As long as it turns in place about 90° and stops for one second and keeps doing that, it's good. Solution code is in [chk2_code.py](chk2_code.py).
4. They should mention some concept of adding up an error over time. Addressing integral windup by constraining the summation's value is highly recommended, but not necessary.
