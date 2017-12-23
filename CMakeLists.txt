cmake_minimum_required(VERSION 3.8)
project(Miller_Rabin)
set(CMAKE_CXX_STANDARD 14)

link_directories(gmp-6.1.2)
add_executable(Miller_Rabin main.cpp)
target_link_libraries(Miller_Rabin gmp)