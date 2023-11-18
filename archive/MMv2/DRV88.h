#ifndef __DRV88_H__
#define __DRV88_H__

#include "mbed.h"

#define THRESH 0.01 // below ~0.18 motor doesn't even move

class DRV88 {
    public:
        DRV88(PinName a1, PinName a2, bool reverse = false, int period_us = 1000);
        void power(float f);
        void brake(float f);
    private:
        PwmOut a1;
        PwmOut a2;
};

#endif