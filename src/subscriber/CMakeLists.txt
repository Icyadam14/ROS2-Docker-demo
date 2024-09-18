cmake_minimum_required(VERSION 3.0.2)
project(subscriber)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
)

catkin_package()

catkin_install_python(PROGRAMS
  src/subscriber.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
