#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
import random


def sample_node():
    pub = rospy.Publisher('random_float_num', Float64, queue_size=10)
    rospy.init_node('sample_node', anonymous=True)
    rate = rospy.Rate(20)  # 20hz
    while not rospy.is_shutdown():
        num = random.uniform(0, 1)
        rospy.loginfo(num)
        pub.publish(num)
        rate.sleep()


if __name__ == '__main__':
    try:
        sample_node()
    except rospy.ROSInterruptException:
        pass
