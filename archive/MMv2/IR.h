#ifndef __IR_H__
#define __IR_H__

#include "mbed.h"
#include <vector>

class IR {
    public:
        static void init(uint32_t period);

        uint16_t reading;

        IR(PinName in, uint8_t discard = 2, uint8_t average = 3);
    private:
        static Thread irThread;
        static uint32_t period;
        static vector<IR*> sensors;
        static void readLoop();

        AnalogIn in;
        uint8_t discard;
        uint8_t average;

        void read();
};

#endif