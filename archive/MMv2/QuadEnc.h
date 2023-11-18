#ifndef __QUADENC_H__
#define __QUADENC_H__

#include "mbed.h"

#define UNITS_PER_SECOND 1.0e6

class QuadEnc {
    public:
        volatile int32_t count; // pulses
        float velocity;

        QuadEnc(PinName a, PinName b, Timer *tim, bool reverse = false);
        void setup();
        void updateVelocity(); // pulses per second
    private:
        InterruptIn a;
        InterruptIn b;
        Timer *tim;
        us_timestamp_t prevTime;
        int32_t prevCount;

        void aRise();
        void aFall();
        void bRise();
        void bFall();
};

#endif