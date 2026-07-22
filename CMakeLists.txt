cmake_minimum_required(VERSION 3.0.2)
project(scara)

find_package(catkin REQUIRED COMPONENTS
  rospy
  roscpp
  std_msgs
  sensor_msgs
  geometry_msgs
)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(
  PROGRAMS
    scripts/forward_kinematics.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
