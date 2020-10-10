import rospy
from std_msgs.msg import Float32

from motor import Motor

WHEEL_PWM = 12
WHEEL_A = 16
WHEEL_B = 18

DRIVE_A = 29
DRIVE_B = 31
DRIVE_PWM = 33

wheel = Motor(WHEEL_A, WHEEL_B, WHEEL_PWM)
drive = Motor(DRIVE_A, DRIVE_B, DRIVE_PWM)


def wheel_callback(data: Float32):
    wheel.drive(data.data)


def drive_callback(data: Float32):
    wheel.drive(data.data)


def driver():
    rospy.init_node("driver")

    rospy.Subscriber("wheel", Float32, wheel_callback)
    rospy.Subscriber("drive", Float32, drive_callback)

    rospy.spin()


if __name__ == '__main__':
    driver()
