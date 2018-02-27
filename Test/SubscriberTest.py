import rospy
from command2ros.msg import MovementCommand

def callback(data):
    #print message to screen, write to node's log file, write to rosout
    rospy.loginfo(rospy.get_caller_id() + ": ", data.data)

def listener():
    #let ros choose unique name for listener
    #allows multiple listeners to run at the same time
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('MovementCommand', MovementCommand, callback)
    rospy.spin()

listener()