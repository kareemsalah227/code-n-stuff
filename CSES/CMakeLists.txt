cmake_minimum_required(VERSION 4.3)
project(CSES)

set(CMAKE_CXX_STANDARD 23)

add_executable(CSES weird-algorithm.cpp
        missing-number.cpp
        repetitions.cpp
        increasing-array.cpp
        permutations.cpp
)
