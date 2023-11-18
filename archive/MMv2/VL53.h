#ifndef __VL53_H__
#define __VL53_H__

#include "mbed.h"
#include "VL53L0X.h"
#include <vector>

class VL53 {
    public:
        static void init(DigitalOut *debugLED = NULL);

        uint16_t dist;

        VL53(I2C *i2c, Timer *tim, PinName r, PinName i);
        void setup(uint8_t addr);
    private:
        static Thread eventThread;
        static EventQueue queue;
        static DigitalOut *debugLED;

        VL53L0X sens;
        DigitalInOut rst;
        InterruptIn irq;

        void getData();
};

#endif