#!/usr/bin/env python

import rospy
from std_msgs.msg import String



def input_publisher(data):
    pub = rospy.Publisher('input data', String, queue_size=10)
    rospy.init_node('input data', anonymous=True)
   
    if not rospy.is_shutdown():
        pub.publish(data)
        print("Done")

if __name__ == '__main__':
    try:
        input_publisher()
    except rospy.ROSInterruptException:
        pass