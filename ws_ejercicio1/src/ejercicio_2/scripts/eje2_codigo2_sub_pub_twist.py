#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist, Point

# el codigo se identifica ante ros
rospy.init_node('sub_pub_node', anonymous=True)

linear_point_pub = rospy.Publisher('linear_point_topic', Point, queue_size=10)
angular_point_pub = rospy.Publisher('angular_point_topic', Point, queue_size=10)

def callback(data):
    linear_point = Point(data.linear.x, data.linear.y, data.linear.z)
    angular_point = Point(data.angular.x, data.angular.y, data.angular.z)

    rospy.loginfo("Valores Lineales (x, y, z): {}, {}, {}".format(linear_point.x, linear_point.y, linear_point.z))
    rospy.loginfo("Valores Angulares (x, y, z): {}, {}, {}".format(angular_point.x, angular_point.y, angular_point.z))

    linear_point_pub.publish(linear_point)
    angular_point_pub.publish(angular_point)

rospy.Subscriber('eje2_codigo1_pub_twist', Twist, callback)

rospy.spin()
