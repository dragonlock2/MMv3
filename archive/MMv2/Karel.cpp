#include "Karel.h"

Karel::Karel(VL53* left, VL53* center, VL53* right, IR* left_ir, IR* right_ir, Motor* motor, float linear_max, float angular_max) :
    left(left), center(center), right(right),
    left_ir(left_ir), right_ir(right_ir),
    motor(motor),
    linear_max(linear_max),
    angular_max(angular_max)
{
    motor->stop();
}

// experimental
void Karel::wallFollowLeft() {
    float wallError = left->dist - 200;
    float wallAng = 0.03 * wallError;

    motor->move(linear_max, wallAng);
}