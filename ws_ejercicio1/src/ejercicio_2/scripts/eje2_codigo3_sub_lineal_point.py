#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Point

def linear_point_callback(data):
    rospy.loginfo("Valores Lineales: x={}, y={}, z={}".format(data.x, data.y, data.z))

def linear_point_subscriber_node():
    rospy.init_node('linear_point_subscriber_node', anonymous=True)
    rospy.Subscriber('linear_point_topic', Point, linear_point_callback)
    rospy.spin()

if __name__ == '__main__':
    linear_point_subscriber_node()
