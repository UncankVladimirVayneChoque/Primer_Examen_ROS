#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Point

def angular_point_callback(data):
    rospy.loginfo("Valores Angulares: x={}, y={}, z={}".format(data.x, data.y, data.z))

def angular_point_subscriber_node():
    rospy.init_node('angular_point_subscriber_node', anonymous=True)
    rospy.Subscriber('angular_point_topic', Point, angular_point_callback)
    rospy.spin()

if __name__ == '__main__':
    angular_point_subscriber_node()
