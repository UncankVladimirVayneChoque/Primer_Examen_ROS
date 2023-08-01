#!/usr/bin/env python3

import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

def main():
    rospy.init_node("c201", anonymous=True)    

    #--------------------------------

    robot = moveit_commander.RobotCommander()        
    scene = moveit_commander.PlanningSceneInterface()
    
    #group_name = rospy.get_param('/c201/Planning_Group') #-------------GROUP NAME
    group_name = "motoman_gp4"
    move_group = moveit_commander.MoveGroupCommander(group_name)
    display_trajectory_publisher = rospy.Publisher(
        "/move_group/display_planned_path",
        moveit_msgs.msg.DisplayTrajectory,
        queue_size=20,
    )
    
    planning_frame = move_group.get_planning_frame()    
    eef_link = move_group.get_end_effector_link()    
    group_names = robot.get_group_names()
    current_state = robot.get_current_state()

     #----------------------------PILAR

    aux_pose = geometry_msgs.msg.PoseStamped()
    aux_pose.header.frame_id = "base_link"
    aux_pose.pose.orientation.w = 1.0
    aux_pose.pose.position.x = 0.6
    aux_pose.pose.position.y = 0.0
    aux_pose.pose.position.z = 0.2
    box_name = "pilar"
    scene.add_box(box_name, aux_pose, size=(0.4, 0.4, 0.4))

    #----------------------------PAREDES

    aux_pose = geometry_msgs.msg.PoseStamped()
    aux_pose.header.frame_id = "base_link"
    aux_pose.pose.orientation.w = 1.0
    aux_pose.pose.position.x = -0.2
    aux_pose.pose.position.y = 1.0
    aux_pose.pose.position.z = 0.5
    box_name = "wall_left"
    scene.add_box(box_name, aux_pose, size=(1.5, 0.1, 1.0))  
    
    aux_pose = geometry_msgs.msg.PoseStamped()
    aux_pose.header.frame_id = "base_link"
    aux_pose.pose.orientation.w = 1.0
    aux_pose.pose.position.x = -1.0
    aux_pose.pose.position.y = 0.0
    aux_pose.pose.position.z = 0.5
    box_name = "wall_bottom"
    scene.add_box(box_name, aux_pose, size=(0.1, 2.0, 1.0))

if __name__ == "__main__":
    main()