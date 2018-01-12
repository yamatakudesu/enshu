import rospy, actionlib
from move_base_msgs.msg import *

if __name__ == '__main__':
    try:
        rospy.init_node('send_goal',anonymous=True)
        client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
        client.wait_for_server()

        goal = MoveBaseGoal()
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.header.frame_id = "/map"
        goal.target_pose.pose.position.x = 3
        goal.target_pose.pose.position.y = 3
        goal.target_pose.pose.orientation.w = 1
        print goal
        client.send_goal(goal)
        print client.wait_for_result(rospy.Duration.from_sec(5.0))
        client.cancel_goal()     
    except rospy.ROSInterruptException: pass
