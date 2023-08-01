#!/usr/bin/env python3
# --------------suscriptor de Float64----------------
import rospy
from geometry_msgs.msg import Point

# el codigo se identifica ante ros
rospy.init_node('eje1_codigo4_sub_point', anonymous=True)	

float_value_1 = 0.0
float_value_2 = 0.0
float_value_3 = 0.0

#se crea la funcion para recibir el mensaje del topico
def callback(data):
    global float_value_1,float_value_2,float_value_3	
    float_value_1 = data.x;
    float_value_2 = data.y;
    float_value_3 = data.z;
    # print(float_value_1, " ", float_value_2, " ", float_value_3)
    rospy.loginfo("x: %f", float_value_1)
    rospy.loginfo("y: %f", float_value_2)
    rospy.loginfo("z: %f", float_value_3)

# se suscribe al topico
sub = rospy.Subscriber("eje1_codigo3_sub_pub_point", Point, callback)
# el codigo point_pub.py publica al topico 'random_point'

rate = rospy.Rate(1) # 1hz --> 1/1hz=1s
while not rospy.is_shutdown():
    rate.sleep() # delay de 1 segundo