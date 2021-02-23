#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import PoseStamped
import math

def talker():
     pub = rospy.Publisher('chatter', PoseStamped, queue_size=10)
     rospy.init_node('talker', anonymous=True)
     rate = rospy.Rate(15) # 15hz
     message = PoseStamped()
     message.pose.position.x = 22
     print(message)
     while not rospy.is_shutdown():
         #theta=rospy.get_time() 

         message.header.frame_id = "map"
         r = 10	
         theta = 0


         while theta < 2*(math.pi):
	       message.pose.position.x = theta
	       message.pose.position.y = math.sin(theta)
               print(message)
               #rospy.loginfo(hello_str)
               pub.publish(message)
               rate.sleep()
               theta = theta + 0.1

         while theta >=0:
	       message.pose.position.x = theta
	       message.pose.position.y = math.sin(-theta)
               print(message)
               #rospy.loginfo(hello_str)
               pub.publish(message)
               rate.sleep()
               theta = theta - 0.1
               print(message)

if __name__ == '__main__':
     try:
         talker()
     except rospy.ROSInterruptException:
         pass
