#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import random

# el codigo se identifica ante ros
rospy.init_node('eje2_codigo1_pub_twist', anonymous=True)

pub = rospy.Publisher('eje2_codigo1_pub_twist', Twist, queue_size=10)

rate = rospy.Rate(1)  # 1 Hz

while not rospy.is_shutdown():
    # Generar valores aleatorios entre -1 y 1 para cada componente de velocidad lineal y angular
    linear_x = random.uniform(-1, 1)
    linear_y = random.uniform(-1, 1)
    linear_z = random.uniform(-1, 1)
    angular_x = random.uniform(-1, 1)
    angular_y = random.uniform(-1, 1)
    angular_z = random.uniform(-1, 1)

    twist_msg = Twist()
    twist_msg.linear.x = linear_x
    twist_msg.linear.y = linear_y
    twist_msg.linear.z = linear_z
    twist_msg.angular.x = angular_x
    twist_msg.angular.y = angular_y
    twist_msg.angular.z = angular_z

    print("Velocidad lineal x: {}, y: {}, z: {}".format(linear_x, linear_y, linear_z))
    print("Velocidad angular x: {}, y: {}, z: {}".format(angular_x, angular_y, angular_z))

    pub.publish(twist_msg)

    rate.sleep()
