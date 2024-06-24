project(KalmanFilter)
cmake_minimum_required(VERSION 3.10)


include_directories(libraries/eigen)

add_executable(KalmanFilter src/main.cpp src/KFilter.cpp)