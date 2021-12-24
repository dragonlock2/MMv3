# Lab 6: More PID

## Background

In the previous lab we were able to get our mice driving a certain distance reasonably straight with just proportional control. This week, we'll learn how to correct for persistent steady state error, turn in place, and follow walls.

Recall our implementation of a **proportional (P) controller** from the last lab.

<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=u%28t%29%20%3D%20K_pe%28t%29">
</p>

Proportional control works pretty well for making our mouse drive straight, but you may have noticed a constant offset error. The motors naturally travel at different speeds given the same power and the constant offset error actually accounts for that difference. If we had zero error, we'd actually apply the same power to each motor, generating an error. How might we fix this? What if we kept track of the total error?

<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=u%28t%29%3DK_pe%28t%29%2BK_i%5Cint_0%5Ete%28%5Ctau%29d%5Ctau">
</p>

This is called a **proportional-integral (PI) controller**. The integral keeps track of the total error (both positive and negative) since we first started the controller. Even small errors will cause the integral term to eventually grow large enough and get <img src="https://render.githubusercontent.com/render/math?math=u%28t%29"> to push our mouse back on track.

In order to dampen oscillations and prevent overshoot, we might want to consider the derivative of our error too. This prevents our error from changing too quickly.

<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=u%28t%29%3DK_pe%28t%29%2BK_i%5Cint_0%5Ete%28%5Ctau%29d%5Ctau%2BK_d%5Cfrac%7Bde%28t%29%7D%7Bdt%7D">
</p>

With these three terms, we have our **proportional-integral-derivative (PID) controller**. <img src="https://render.githubusercontent.com/render/math?math=K_p">, <img src="https://render.githubusercontent.com/render/math?math=K_i">, and <img src="https://render.githubusercontent.com/render/math?math=K_d"> are tunable gains that determine the behavior of our error (rise time, peak, overshoot, etc.).

Let's go over what each of the terms in PID means.

* The **P** term (**proportional**) increases our correction proportionally to the error: the higher our error, the more power we should apply to correct for it.
* The **I** term (**integral**) compensates for long-term error and drift by integrating the error over time. While a small tendency for our mouse to veer to the right might have little effect on the P term, it’ll cause the I term to build up until the system reaches the setpoint perfectly.
* The **D** term (**derivative**) takes the derivative of the error with respect to time. Systems often have inertia: the faster our error is already decreasing, the less power we need to apply to correct for it. This dampens our controller and reduces overshooting.

Note this checkpoint has no code.

### Checkoff #1

1. We only have individual measurements of error, not a continuous function. How might we estimate the integral of the error?
2. How might we estimate the derivative of the error?
3. One potential issue with PID control is **integral windup**. You can read about it [here](https://en.wikipedia.org/wiki/Integral_windup). What are some ways of preventing integral windup?

## Turning

Copy over the skeleton code in [labs/lab6/](../labs/lab6) onto your mouse. To encourage code readability, we've added a couple of function definitions that modularize the controller. Adapt your P controller code from [Lab 5](lab5.md) to these functions by filling out the TODOs. If you have a better way of organizing the functions, feel free to change things. Ultimately, it should have the same behavior as Checkoff #2 from Lab 5.

Next, add I and D terms to both your angular and linear P controllers. You may find the `global` or `nonlocal` keywords to be useful for accessing variables defined outside of a function. We highly recommend just tuning the PID constants for your linear controller first and then tuning the angular controller when you implement turning. It's generally easier when that specific controller is being exercised. Good starting values are 10x smaller than <img src="https://render.githubusercontent.com/render/math?math=K_p">.

Finally, have your mouse turn 90° in place. This should be as simple as setting a different target <img src="https://render.githubusercontent.com/render/math?math=%5Ctheta">. For an added challenge, let's create a `turn_left` function which internally loops until the mouse turns about 90° (you choose the threshold for acceptable error) before returning. You may find it useful to be able to reset the odometry back to 0 with the following function.

```python
def reset_odometry():
    lenc.position, renc.position = 0, 0
```

### Checkoff #2

1. Demonstrate your working PID loop driving straight a set distance.
2. Demonstrate your working PID loop turning in place by 90°.
3. Demonstrate turning in place by 90° and then stopping for one second before turning another 90° and so on.
4. Explain your implementation of your integral term. Did you account for integral windup?

## Wall Following

When we're driving in a maze, our mouse will always be slightly misaligned with reference to a wall. Despite driving perfectly straight, this slight error will eventually cause us to crash. By performing feedback control with our IR sensors, we can correct for any misalignment!

In the interest of developing maze solving primitives in the future, you will implement a `forward()` function that will have the mouse drive forwards 180mm and stop. While driving forward, maintain a fixed 45mm distance from a wall on the left.

Optimally, stable wall following means maintaining a 0° angle with respect to the wall. With just one sensor, it's impossible to determine the angle because multiple angles can correspond to the same sensed distance. Performing feedback control on just that sensor works, but it relies on the mouse moving a bit to correct for angular errors. With two sensors, we can determine the angle from the wall based on the difference between the sensors. Wall following could then be implemented as just setting the angle of the mouse based on the distance error and letting its forward motion correct for the distance error.

To implement wall following, start by taking your distance measurement code from lab 3 and your linear and angular PID controllers from the previous checkoff. Conceptually, we want to change the definitions of `theta` and `theta_target` for the angular controller. Based on what was discussed previously, what are the new definitions of `theta` and `theta_target`?

Don't worry about implementing a PID controller for this as a P controller is adequate. Tuning can be a bit tricky. We've found that `Kp_theta=0.01` and `Kp_ang=0.01` work pretty well. Our reference solution uses `Kp_theta` to scale the distance error to set `theta_target`. Since we assume the mouse drives pretty straight and isn't very misaligned, don't worry about tuning your controller to work well for large errors.

### Checkoff #3

1. Demonstrate your wall following code by calling `forward()` once every second.
2. How might you extend your code to drive straight in between two walls?
