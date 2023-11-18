#ifndef __MOTOR_H__
#define __MOTOR_H__

#include "mbed.h"
#include "QuadEnc.h"
#include "DRV88.h"

#define TICKS_PER_REV 218 //870 (X4), using X1 encoding bc much more stable, but gives ~1mm accuracy
#define PI 3.14159265359
#define WHEEL_DIAMETER 34 //mm
#define MOUSE_DIAMETER 82 //mm

class Motor {
    public:
        Motor(QuadEnc* leftenc, QuadEnc* rightenc, DRV88* leftmot, DRV88* rightmot);

        void init(uint32_t period);
        void setLinearPID(float kp, float ki, float kd);
        void setAngularPID(float kp, float ki, float kd);
        void setLinearIntegralConstraint(float ki_constr);
        void setAngularIntegralConstraint(float ki_constr);
        void move(float linearTarget, float angularTarget);
        void stop();

        float getLinearVelocity(); // mm/s
        float getAngularVelocity(); // rad/s
    private:
        Thread thread;
        uint32_t _period;
        float _linearTarget, linear_kp, linear_ki, linear_kd, linear_ki_constr;
        float _angularTarget, angular_kp, angular_ki, angular_kd, angular_ki_constr;
        bool brake;
        QuadEnc* leftenc;
        QuadEnc* rightenc;
        DRV88* leftmot;
        DRV88* rightmot;

        void pidLoop();
        float ticksToMM(float ticks);
        float constrainAbs(float val, float constr);
};

#endif