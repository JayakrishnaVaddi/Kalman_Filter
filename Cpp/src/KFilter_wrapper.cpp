#include<pybind11/pybind11.h>
#include<pybind11/eigen.h>
#include "KFilter.hpp"

double add(double int1, double int2)
{
    return int1+int2;
}

PYBIND11_MODULE(KFilter_cpp, kf)
{
    kf.doc() = "Just a Kalman Filter code in Cpp";
    kf.def("add", &add, "Just adding function");
    pybind11::class_<KFilter>(kf, "KFilter")
        .def(pybind11::init<double, double, double>())
        .def("raw_estimates", &KFilter::raw_estimates)
        .def("update_estimate", &KFilter::update_estimate)
        .def_property_readonly("cov", &KFilter::cov)
        .def_property_readonly("mean", &KFilter::mean)
        .def_property_readonly("position", &KFilter::position)
        .def_property_readonly("velocity", &KFilter::velocity);
}
