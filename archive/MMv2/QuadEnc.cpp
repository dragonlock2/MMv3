#include "QuadEnc.h"

QuadEnc::QuadEnc(PinName a, PinName b, Timer *tim, bool reverse) :
    a(reverse ? b : a),
    b(reverse ? a : b),
    tim(tim)
{}

void QuadEnc::setup() {
    // really easy to change to other encodings, just comment some of these lines out
    a.rise(callback(this, &QuadEnc::aRise));
    // a.fall(callback(this, &QuadEnc::aFall));
    // b.rise(callback(this, &QuadEnc::bRise));
    // b.fall(callback(this, &QuadEnc::bFall));

    count = 0;
    velocity = 0;
    prevTime = tim->read_high_resolution_us();
    prevCount = 0;
}

void QuadEnc::updateVelocity() {
    velocity = UNITS_PER_SECOND * (count - prevCount) / (tim->read_high_resolution_us() - prevTime);
    prevTime = tim->read_high_resolution_us();
    prevCount = count;
}

void QuadEnc::aRise() {
    count += b.read() ? -1 : 1;
}

void QuadEnc::aFall() {
    count += b.read() ? 1 : -1;
}

void QuadEnc::bRise() {
    count += a.read() ? 1 : -1;
}

void QuadEnc::bFall() {
    count += a.read() ? -1 : 1;
}