#ifndef __KAREL_H__
#define __KAREL_H__

#include "mbed.h"
#include "VL53.h"
#include "IR.h"
#include "Motor.h"

class Karel {
    public:
        Karel(VL53* left, VL53* center, VL53* right, IR* left_ir, IR* right_ir, Motor* motor, float linear_max, float angular_max);

        // experimental
        void wallFollowLeft();
    private:
        VL53 *left, *center, *right;
        IR *left_ir, *right_ir;
        Motor* motor;
        float linear_max, angular_max;
};

#endif