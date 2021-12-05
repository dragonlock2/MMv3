# Lab 5: Intro to PID

## Background

You may have noticed that if you let your mouse drive forward for long enough, it'll start drifting to one side. That's because we're just using open-loop control where we apply some input and hope we get the desired output. For various reasons, including but not limited to the following, our mouse will not drive straight even given the same power to both motors.

* The mouse isn't perfectly balanced as all things should be.
* The ground is not perfectly flat.
* Our motors aren't exactly the same.

To fix this, we'll apply something called closed-loop control. Also known as feedback control, we take measurements from the encoders to adjust the power to our motors and drive straight. For example, if we are veering to the left based on encoder readings, we can increase power to the left motor and decrease power to the right motor to correct it.

One common way to do feedback control is PID. For now, you'll be implementing just the P part of it. Conceptually, feedback controllers try to minimize some error which is the difference between a measured value (aka process variable) and setpoint.

For a P controller, we vary our motor power proportionally to our error. That is, the larger our error, the more power we apply to correct for it.

<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=u%28t%29%20%3D%20K_pe%28t%29">
</p>

## Drive Straight

Copy over the skeleton code in [labs/lab5/](../labs/lab5) onto your mouse. Our code is getting too long to just copy paste every time. By default, the code makes the mouse drive forward at 20% speed. Next, copy over your code from [Lab 4](lab4.md) to compute `dist` and `theta` based on encoder readings.

Your job is to apply P control to make the mouse drive straight. The linear velocity doesn't matter too much, just the fact that it doesn't veer left or right. To do this, it would help to answer the following questions.

* What is <img src="https://render.githubusercontent.com/render/math?math=%5Ctheta"> when driving straight?
* What is the error when driving straight?
* Given an error, how do you change each motor's power to correct for it?

When implementing the P controller, start with <img src="https://render.githubusercontent.com/render/math?math=K_p"> values of around 0.1 and tune up and down from there based on performance. To make sure the mouse does move forward, add 0.2 to the `throttle` for each motor in addition to your correction term.

### Checkoff #1

1. Demonstrate your working P controller. Print out your error term too.
2. How do you compute the error term?
3. If we want our applied correction power <img src="https://render.githubusercontent.com/render/math?math=u%28t%29"> to be maximized (<img src="https://render.githubusercontent.com/render/math?math=u%28t%29%3D1">) when the error is 2 radians, what is <img src="https://render.githubusercontent.com/render/math?math=K_p">?
4. What happens when <img src="https://render.githubusercontent.com/render/math?math=K_p"> is too low? How about too high? What value did you end up using?

## Go the Distance

When solving mazes, it is quite useful to be able to drive forward a set distance. Let's swap out the 0.2 we blindly added to the `throttle` for a linear correction term. Your job is to get your mouse to drive straight forward 200mm and then stop. Like with driving straight, it'd help to answer the following questions.

* What is the error for traveling a set distance?
* Given an error, how do you change each motor's power to correct for it?

When implementing the P controller, start with <img src="https://render.githubusercontent.com/render/math?math=K_p"> values of 0.1 and tune. Don't remove your angular correction code from before since we still want to drive straight. Since we want to leave a little wiggle room for the angular correction, limit the linear correction term to around 0.9.

### Checkoff #2

1. Demonstrate your working P controller. Print out your error term too.
2. How do you compute the error term?
3. If we want our applied correction power <img src="https://render.githubusercontent.com/render/math?math=u%28t%29"> to be maximized (<img src="https://render.githubusercontent.com/render/math?math=u%28t%29%3D1">) when the error is 100mm, what is <img src="https://render.githubusercontent.com/render/math?math=K_p">?
