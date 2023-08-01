#!/usr/bin/env python3
#--------------publicador de Int32--------------
import rospy
from std_msgs.msg import Int32
import random

# el codigo se identifica ante ros
rospy.init_node('eje1_codigo1_pub_int', anonymous=True)

# se crea el topico publicador
pub = rospy.Publisher('eje1_codigo1_pub_int', Int32, queue_size=1)
# pub = rospy.Publisher('nombre-topico', tipo-mensaje, queue_size=1)

rate = rospy.Rate(1) # 1hz --> 1/1hz=1s
while not rospy.is_shutdown():
    valor=random.randint(1,100)
    rospy.loginfo(valor)
    pub.publish(valor) 
    rate.sleep() # delay de 1 segundo