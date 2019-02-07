import rospy
from std_msgs.msg import Char 

class DriveMotorAPI:
    FORWARD = 1
    BACKWARD = 2

    CLOCKWISE = -1
    COUNTERCLOCKWISE = 3

    def __init__(self):
        #init publishers for direction & speed topics
        self.speedPublisher = rospy.Publisher("driveSpeed", Char, queue_size=5)
        self.dirPublisher = rospy.Publisher("driveDirection", Char, queue_size=5)
        #init ROS node 
        rospy.init_node("driveMotorAPI")
        return

    #set direction to backwards & intended speed to 100/127
    def driveBackwards(self):
        self.dirPublisher.publish(self.BACKWARD)
        self.speedPublisher.publish(100)

    #set direction to forwards & intended speed to 100/127
    def driveForwards(self):
        self.dirPublisher.publish(self.FORWARD)
        self.speedPublisher.publish(100)

    #set intended speed to 0
    def stop(self):
        self.speedPublisher.publish(0)

    #set direction to cw or ccwxe
    #TODO: check validity of interpretation and check "turn" vs "spin" <- in place or while moving
    def turn(self, direction):
        if(direction == self.CLOCKWISE or direction == self.COUNTERCLOCKWISE):
            self.dirPublisher.publish(direction)

if __name__ == '__main__':
    try:
        d = DriveMotorAPI()
    except rospy.ROSInterruptException:
        pass