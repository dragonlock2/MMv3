#include "DRV88.h"

DRV88::DRV88(PinName a1, PinName a2, bool reverse, int period_us) :
    a1(reverse ? a2 : a1),
    a2(reverse ? a1: a2)
{
    this->a1.period_us(period_us);
    this->a2.period_us(period_us);
    this->a1 = 0;
    this->a2 = 0;
}

// -1 for full speed back, 1 for full speed forward
void DRV88::power(float f) {
    if (f > 1.0) {
        f = 1.0;
    } else if (f < -1.0) {
        f = -1.0;
    }

    if (f > THRESH) {
        a1 = 0;
        a2 = f;
    } else if (f < -THRESH) {
        a1 = -f;
        a2 = 0;
    } else {
        a1 = 0;
        a2 = 0;
    }
}

// 0 for coast, 1 for hard brake
void DRV88::brake(float f) {
    if (f < 0.0) {
        f = 0.0;
    } else if (f > 1.0) {
        f = 1.0;
    }

    a1 = f;
    a2 = f;
}