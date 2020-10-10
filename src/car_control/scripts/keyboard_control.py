# Simple talker demo that published std_msgs/Strings messages
# to the 'chatter' topic

import os

import rospy
from std_msgs.msg import Float32


def control():
    wheel = rospy.Publisher('wheel', Float32, queue_size=10)
    drive = rospy.Publisher('drive', Float32, queue_size=10)

    cmd_fwd = 0
    cmd_left = 0

    rospy.init_node('keyboard_control', anonymous=True)
    while not rospy.is_shutdown():
        key = input("Command the Vehicle (WASD)")
        if key in ["w"]:
            cmd_fwd = 1
        elif key in ["s"]:
            cmd_fwd = -1
        elif key in ["a"]:
            cmd_left = 1
        elif key in ["d"]:
            cmd_left = -1
        else:
            cmd_fwd = 0
            cmd_left = 0
            print(f"Clearing Input")

        wheel.publish(cmd_left)
        drive.publish(cmd_fwd)
        print(f"FWD: {cmd_fwd}, LEFT:: {cmd_left}")


if __name__ == '__main__':
    try:
        control()
    except rospy.ROSInterruptException:
        pass
