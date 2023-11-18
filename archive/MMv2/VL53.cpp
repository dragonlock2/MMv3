#include "VL53.h"

Thread VL53::eventThread(osPriorityBelowNormal, 256);
EventQueue VL53::queue;
DigitalOut *VL53::debugLED;

void VL53::init(DigitalOut *debugLED) {
    VL53::debugLED = debugLED;
    eventThread.start(callback(&queue, &EventQueue::dispatch_forever));
}

VL53::VL53(I2C *i2c, Timer *tim, PinName r, PinName i) :
    sens(i2c, tim),
    rst(r, PIN_OUTPUT, PullNone, 0),
    irq(i),
    dist(0)
{}

void VL53::setup(uint8_t addr) {
    irq.fall(queue.event(this, &VL53::getData)); // i2c don't work in ISR
    rst = 1; // 3v3 ok
    ThisThread::sleep_for(2); // tboot <= 1.2ms
    sens.setAddress(addr);
    sens.setTimeout(100);
    sens.init();
    sens.startContinuous();
}

void VL53::getData() {
    if (debugLED != NULL) {
        *debugLED = !(*debugLED);
    }
    uint16_t temp = sens.readReg16Bit(sens.RESULT_RANGE_STATUS + 10);
    sens.writeReg(sens.SYSTEM_INTERRUPT_CLEAR, 0x01);
    if (temp < 2000) {
        dist = temp; // filter out bad readings
    }
}