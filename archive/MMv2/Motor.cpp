#include "Motor.h"

Motor::Motor(QuadEnc* leftenc, QuadEnc* rightenc, DRV88* leftmot, DRV88* rightmot) :
    leftenc(leftenc),
    rightenc(rightenc),
    leftmot(leftmot),
    rightmot(rightmot),
    thread(osPriorityNormal, 256),
    _period(0),
    _linearTarget(0), _angularTarget(0),
    linear_kp(0), linear_ki(0), linear_kd(0), linear_ki_constr(1000),
    angular_kp(0), angular_ki(0), angular_kd(0), angular_ki_constr(1000),
    brake(false)
{}

void Motor::init(uint32_t period) {
    _period  = period;
    thread.start(callback(this, &Motor::pidLoop));
}

void Motor::pidLoop() {
    float linear_err, linear_correction;
    float linear_err_prev, linear_deriv;
    float linear_integral = 0.0;

    float angular_err, angular_correction;
    float angular_err_prev, angular_deriv;
    float angular_integral = 0.0;

    while (1) {
        if (brake) {
            leftmot->brake(1);
            rightmot->brake(1);
        } else {
            leftenc->updateVelocity();
            rightenc->updateVelocity();

            linear_err = _linearTarget - getLinearVelocity();
            linear_integral += linear_err;
            linear_integral = constrainAbs(linear_integral, linear_ki_constr);
            linear_deriv = linear_err - linear_err_prev;
            linear_err_prev = linear_err;
            linear_correction = linear_kp * linear_err + linear_ki * linear_integral + linear_kd * linear_deriv;

            angular_err = _angularTarget - getAngularVelocity();
            angular_integral += angular_err;
            angular_integral = constrainAbs(angular_integral, angular_ki_constr);
            angular_deriv = angular_err - angular_err_prev;
            angular_err_prev = angular_err;
            angular_correction = angular_kp * angular_err + angular_ki * angular_integral + angular_kd * angular_deriv;

            leftmot->power(linear_correction - angular_correction);
            rightmot->power(linear_correction + angular_correction);
        }

        ThisThread::sleep_for(_period);
    }
}

void Motor::move(float linearTarget, float angularTarget) {
    _linearTarget = linearTarget;
    _angularTarget = angularTarget;
    brake = false;
}

void Motor::stop() {
    brake = true;
}

void Motor::setLinearPID(float kp, float ki, float kd) {
    linear_kp = kp;
    linear_ki = ki;
    linear_kd = kd;
}

void Motor::setAngularPID(float kp, float ki, float kd) {
    angular_kp = kp;
    angular_ki = ki;
    angular_kd = kd;
}

void Motor::setLinearIntegralConstraint(float ki_constr) {
    linear_ki_constr = ki_constr;
}

void Motor::setAngularIntegralConstraint(float ki_constr) {
    angular_ki_constr = ki_constr;
}

float Motor::getLinearVelocity() {
    return (ticksToMM(leftenc->velocity) + ticksToMM(rightenc->velocity)) / 2;
}

float Motor::getAngularVelocity() {
    return (ticksToMM(rightenc->velocity) - ticksToMM(leftenc->velocity)) / MOUSE_DIAMETER;
}

float Motor::ticksToMM(float ticks) {
    return ticks / TICKS_PER_REV * PI * WHEEL_DIAMETER;
}

float Motor::constrainAbs(float val, float constr) {
    if (val < -constr) {
        return -constr;
    } else if (val > constr) {
        return constr;
    } else {
        return val;
    }
}