#!/usr/bin/env python3
# --------------suscriptor de Float64----------------
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import Float64
from geometry_msgs.msg import Point

# el codigo se identifica ante ros
rospy.init_node('eje1_codigo3_sub_pub_point', anonymous=True)	

int_value_1 = 0
float_value_1 = 0 
float_value_2 = 0
res_value_3 = 0

def callback1(data1):
    global int_value_1
    int_value_1 = data1.data

def callback2(data2):
    global float_value_2
    float_value_2 = data2.data

# se suscribe al topico
sub = rospy.Subscriber("eje1_codigo1_pub_int", Int32, callback1)
sub = rospy.Subscriber("eje1_codigo2_pub_float", Float64, callback2)

pub = rospy.Publisher('eje1_codigo3_sub_pub_point', Point, queue_size=10)

rate = rospy.Rate(1)  # 1 Hz

while not rospy.is_shutdown():
    float_value_1 = float(int_value_1)  
    res_value_3 = int_value_1 + float_value_2
    punto = Point(float_value_1, float_value_2, res_value_3)
    rospy.loginfo("x: %f", float_value_1)
    rospy.loginfo("y: %f", float_value_2)
    rospy.loginfo("z: %f", res_value_3)
    pub.publish(punto)
    rate.sleep()
