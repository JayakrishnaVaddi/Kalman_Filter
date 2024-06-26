#include<iostream>
#include<pybind11/pybind11.h>

double add(double int1, double int2)
{
    return int1+int2;
}

PYBIND11_MODULE(KFilter_cpp, kf )
{
    kf.doc() = "Just a Kalman Filter code in Cpp";
    kf.def("add", &add, "Just adding function");

}