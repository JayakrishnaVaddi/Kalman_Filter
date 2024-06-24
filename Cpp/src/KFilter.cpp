#include <iostream>
#include <Eigen/Dense>
#include "KFilter.hpp"

using vector = Eigen::Matrix<double, 2, 1>;
using matrix = Eigen::Matrix<double, 2, 2>;


KFilter::KFilter(double initial_x, double initial_v, double accel_variance)
{
    state_values<< initial_x, initial_v;
    covariences << 1, 0, 0, 1;

    accelVariance = accel_variance;
}

void KFilter::raw_estimates(double dt)
{
    matrix F;
    vector G;
    F<< 1, dt, 0, 1;
    G<< 0.5*dt*dt, dt;

    vector new_x = F*state_values;
    matrix new_p = F*covariences*F.transpose() + G* G.transpose() *  accelVariance;

    state_values = new_x;
    covariences = new_p;

}
void KFilter::update_estimate(double meas_position, double meas_variance)
{

    Eigen::Matrix<double, 1, 2> H;
    H << 1,0;
    Eigen::Matrix<double, 1, 1> z;
    z << meas_position;
    Eigen::Matrix<double, 1, 1> R;
    Eigen::Matrix<double, 1, 1> Y;
    Eigen::Matrix<double, 1, 1> s;
    Eigen::Matrix<double, 2, 1> k;   
    matrix I;
    I.setIdentity(); 

    Y = z - (H*state_values);
    s = (H*covariences* H.transpose()) + R;

    k = covariences* H.transpose()*s.inverse();


    vector new_x = state_values + k*Y;
    matrix new_p = (I - k*H) *covariences;

    state_values = new_x;
    covariences = new_p;

}
matrix KFilter::cov()
{
    return covariences;
}
vector KFilter::mean()
{
    return state_values;
}
double KFilter::position()
{
    return state_values[0];
}
double KFilter::velocity()
{
    return state_values[1];
}
