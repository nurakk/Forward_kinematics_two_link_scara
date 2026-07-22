# SCARA Robot Forward Kinematics using URDF and RViz (ROS Noetic)

## Project Overview

This project demonstrates the Forward Kinematics of a 3-DOF SCARA (Selective Compliance Assembly Robot Arm) robot using ROS Noetic on Ubuntu 20.04. The robot is modeled using URDF and visualized in RViz. Joint movements are controlled using **joint_state_publisher_gui**, while a Python node continuously computes and displays the end-effector position using Forward Kinematics equations.

**Platform:** Ubuntu 20.04
**ROS Version:** ROS Noetic
**Workspace:** `proj3`
**Package:** `scara`

---

# Features

* 3-DOF Standing SCARA Robot
* URDF Robot Modeling
* RViz Visualization
* Joint State Publisher GUI
* Robot State Publisher
* Real-Time Forward Kinematics
* Python Implementation
* ROS Noetic Compatible
* Ubuntu 20.04 Compatible
* No Gazebo Required

---

# Software Requirements

* Ubuntu 20.04
* ROS Noetic
* Python 3
* RViz
* URDF
* joint_state_publisher_gui
* robot_state_publisher

---

# Workspace Creation

```bash
mkdir -p ~/proj3/src

cd ~/proj3

catkin_make

source devel/setup.bash
```

(Optional)

```bash
echo "source ~/proj3/devel/setup.bash" >> ~/.bashrc

source ~/.bashrc
```

---

# Package Creation

```bash
cd ~/proj3/src

catkin_create_pkg scara rospy roscpp std_msgs sensor_msgs geometry_msgs urdf xacro robot_state_publisher joint_state_publisher
```

---

# Create Project Folders

```bash
cd ~/proj3/src/scara

mkdir launch

mkdir scripts

mkdir urdf

mkdir rviz
```

---

# Project Directory Structure

```text
proj3
│
└── src
    │
    └── scara
        │
        ├── launch
        │      └── display.launch
        │
        ├── scripts
        │      └── forward_kinematics.py
        │
        ├── urdf
        │      └── scara.urdf
        │
        ├── rviz
        │
        ├── package.xml
        │
        ├── CMakeLists.txt
        │
        └── README.md
```

---

# Python Script Permission

```bash
cd ~/proj3/src/scara/scripts

chmod +x forward_kinematics.py
```

---

# Build the Workspace

```bash
cd ~/proj3

catkin_make
```

---

# Source the Workspace

```bash
source devel/setup.bash
```

---

# Launch the Project

```bash
roslaunch scara display.launch
```

---

# Robot Configuration

```
             End Effector
                  ●
                  │
                  │
           Prismatic Joint
                  │
        ---------------------
              Link 2
             /
            /
      --------------------
            Link 1
               │
               │
         Revolute Joint
               │
           Base Link
```

---

# Robot Degrees of Freedom

| Joint   | Type      | Motion                   |
| ------- | --------- | ------------------------ |
| Joint 1 | Revolute  | Rotation about Z-axis    |
| Joint 2 | Revolute  | Rotation about Z-axis    |
| Joint 3 | Prismatic | Translation along Z-axis |

---

# Link Dimensions

| Link   | Length |
| ------ | ------ |
| Link 1 | 0.30 m |
| Link 2 | 0.30 m |

---

# ROS Nodes

* joint_state_publisher_gui
* robot_state_publisher
* forward_kinematics.py
* RViz

---

# ROS Topics

## Subscribed

```
/joint_states
```

## Published

```
/tf
/tf_static
```

---

# Useful ROS Commands

## Verify Package

```bash
rospack find scara
```

## View Running Nodes

```bash
rosnode list
```

## View Available Topics

```bash
rostopic list
```

## Monitor Joint States

```bash
rostopic echo /joint_states
```

## Generate TF Tree

```bash
rosrun tf view_frames
```

## View ROS Graph

```bash
rqt_graph
```

---

# Forward Kinematics

The SCARA robot forward kinematics is given by

```
x = L1 cos(θ1) + L2 cos(θ1 + θ2)

y = L1 sin(θ1) + L2 sin(θ1 + θ2)

z = d3
```

where

* L1 = Length of Link 1
* L2 = Length of Link 2
* θ1 = Joint 1 Angle
* θ2 = Joint 2 Angle
* d3 = Prismatic Joint Displacement

---

# Sample Terminal Output

```
Forward Kinematics Node Started

Joint 1 = 30.00°

Joint 2 = 45.00°

Joint 3 = 0.100 m

End Effector Position

X = 0.472 m

Y = 0.440 m

Z = 0.100 m
```

---

# Applications

* Industrial Robotics
* Robot Kinematics
* Robotics Education
* ROS Learning
* Manipulator Simulation
* Automation Research

---

# Future Enhancements

* Inverse Kinematics
* Jacobian Matrix
* Trajectory Planning
* MoveIt Integration
* Pick and Place
* Gripper Attachment
* Cartesian Motion Planning
* Workspace Analysis

---

# Author

**Arun K**

Assistant Professor

Department of Robotics and Automation

ROS | Python | URDF | RViz

---

# License

This project is intended for educational and research purposes.
