#include "mbed.h"

// Custom classes
#include "VL53.h"
#include "QuadEnc.h"
#include "DRV88.h"
#include "IR.h"
#include "Motor.h"
#include "Karel.h"

// Debug
DigitalOut red(PC_15, 1); // note inverted
DigitalOut green(PC_14, 1);
DigitalOut blue(PC_13, 1);
Serial pc(PA_9, PA_10);

// RTOS
Timer tim;

// Sensors
I2C i2c(PB_11, PB_10);
VL53 left(&i2c, &tim, PB_1, PB_2); // XSHUT, GPIO
VL53 center(&i2c, &tim, PA_4, PA_5);
VL53 right(&i2c, &tim, PA_2, PA_3);

IR left_ir(PA_7);
IR right_ir(PA_0);

QuadEnc leftenc(PB_7, PB_6, &tim);
QuadEnc rightenc(PB_9, PB_8, &tim, true);

// Outputs
DRV88 leftdrv(PB_5, PB_4, true);
DRV88 rightdrv(PA_15, PB_3);

Motor motor(&leftenc, &rightenc, &leftdrv, &rightdrv);

int main()
{
    pc.baud(115200);

    i2c.frequency(125000);

    tim.start();

    // Sensor Setup
    VL53::init(&red);
    left.setup(0x01);
    center.setup(0x02);
    right.setup(0x03);

    IR::init(5); // ~200Hz polling

    rightenc.setup();
    leftenc.setup();
    ThisThread::sleep_for(10);

    // Output Setup
    motor.init(5); // ~200Hz PID
    motor.setLinearPID(0.005, 0.005, 0.0);
    motor.setLinearIntegralConstraint(200);
    motor.setAngularPID(0.1, 0.1, 0.0); // 0.1
    motor.setAngularIntegralConstraint(10);

    Karel karel(&left, &center, &right, &left_ir, &right_ir, &motor, 1000, 24);

    // Test
    // motor.move(1000, 0);
    // motor.move(0, 24);

    while (true) {
        // leftenc.updateVelocity();
        // rightenc.updateVelocity();

        // pc.printf("%d %f %d %f\n", leftenc.count, leftenc.velocity, rightenc.count, rightenc.velocity;
        // pc.printf("%d %d %d\n", left.dist, center.dist, right.dist);
        // pc.printf("%d %d\n", left_ir.reading, right_ir.reading);

        // pc.printf("%d %f %d %f %d %d %d %d %d\n", leftenc.count, leftenc.velocity, rightenc.count, rightenc.velocity, 
        //     left.dist, center.dist, right.dist, 
        //     left_ir.reading, right_ir.reading);

        // pc.printf("%f %f\n", motor.getLinearVelocity(), motor.getAngularVelocity() * 100);

        karel.wallFollowLeft();

        ThisThread::sleep_for(20);
    }
}