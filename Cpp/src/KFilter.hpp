#include <iostream>
#include <Eigen/Dense>

class KFilter
{   
    using vector = Eigen::Matrix<double, 2, 1>;
    using matrix = Eigen::Matrix<double, 2, 2>;

private:
    vector state_values;
    matrix covariences;

    double accelVariance;

public:
    KFilter(double initial_x, double initial_v, double accelVariance);
    void raw_estimates(double dt);
    void update_estimate(double meas_position, double meas_variance);
    matrix cov();
    vector mean();
    double position();
    double velocity();
};