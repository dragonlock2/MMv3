#include "IR.h"

Thread IR::irThread(osPriorityBelowNormal, 256);
uint32_t IR::period = 0;
vector<IR*> IR::sensors;

void IR::init(uint32_t period) {
    IR::period = period;
    irThread.start(IR::readLoop);
}

void IR::readLoop() {
    while (true) {
        for (auto i = sensors.begin(); i != sensors.end(); i++) {
            (*i)->read();
        }

        ThisThread::sleep_for(period);
    }
}

IR::IR(PinName in, uint8_t discard, uint8_t average) :
    reading(0),
    in(in),
    discard(discard),
    average(average)
{
    sensors.push_back(this);
}

void IR::read() {
    uint8_t i;
    for (i = 0; i < discard; i++) {
        in.read_u16();
    }
    uint32_t avg = 0;
    for (i = 0; i < average; i++) {
        avg += in.read_u16();
    }
    reading = avg / average;
}