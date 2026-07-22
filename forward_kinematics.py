#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import JointState
import math

# Link lengths (meters)
L1 = 0.30
L2 = 0.30

# Joint variables
theta1 = 0.0
theta2 = 0.0
d3 = 0.0


def joint_callback(msg):
    global theta1, theta2, d3

    try:
        # Read joint values by name
        joint_dict = dict(zip(msg.name, msg.position))

        theta1 = joint_dict.get("joint1", 0.0)
        theta2 = joint_dict.get("joint2", 0.0)
        d3 = joint_dict.get("joint3", 0.0)

        # Forward Kinematics
        x = L1 * math.cos(theta1) + L2 * math.cos(theta1 + theta2)
        y = L1 * math.sin(theta1) + L2 * math.sin(theta1 + theta2)
        z = -d3   # downward motion

        rospy.loginfo("--------------------------------------")
        rospy.loginfo("Joint 1 = %.2f deg", math.degrees(theta1))
        rospy.loginfo("Joint 2 = %.2f deg", math.degrees(theta2))
        rospy.loginfo("Joint 3 = %.3f m", d3)

        rospy.loginfo("End Effector Position")
        rospy.loginfo("X = %.3f m", x)
        rospy.loginfo("Y = %.3f m", y)
        rospy.loginfo("Z = %.3f m", z)

    except Exception as e:
        rospy.logwarn(str(e))


def main():

    rospy.init_node("forward_kinematics")

    rospy.Subscriber("/joint_states", JointState, joint_callback)

    rospy.loginfo("Forward Kinematics Node Started")

    rospy.spin()


if __name__ == "__main__":
    main()
