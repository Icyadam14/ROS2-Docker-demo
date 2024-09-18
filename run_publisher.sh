#!/bin/bash

colcon build --build-base /build --install-base /install
source /install/setup.bash
ros2 run publisher publisher.py