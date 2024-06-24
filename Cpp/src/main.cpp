#include <iostream>
#include <Eigen/Dense>
#include "KFilter.hpp"


int main()
{   
    using matrix = Eigen::Matrix<double, 2, 2>;
    using vector = Eigen::Matrix<double, 2,1 >;
    KFilter kf(5, 0.2, 1.2);

    double position = kf.position();
    
    kf.raw_estimates(0.1);

    matrix covarience = kf.cov();
    return 0;
}