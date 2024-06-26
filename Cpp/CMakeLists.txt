project(KalmanFilter)
cmake_minimum_required(VERSION 3.10)

add_subdirectory(libraries/pybind11)
include_directories(libraries/eigen)

pybind11_add_module(kfilter_cpp src/KFilter_wrapper.cpp)

add_executable(KalmanFilter src/main.cpp src/KFilter.cpp)