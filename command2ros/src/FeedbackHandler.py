#!/usr/bin/env python3

import rospy
from command2ros.msg import MovementFeedback
from MovementFeedbackData import MovementFeedbackData
import threading

class FeedbackHandler(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.messageQueue = []
        return

    def run(self):
        self.listener()

    def movementFeedbackCallback(self, data):
        feedback = MovementFeedbackData()
        feedback.ready = data.ready
        feedback.messageID = data.messageID
        feedback.serialID = data.serialID
        feedback.msg = data.msg
        self.messageQueue.append(feedback)

    def mv2ImageCallback(self, data):
        x = True #so it compiles
        #handle returned image data here

    def listener(self):
        rospy.Subscriber("MovementFeedback", MovementFeedback, self.movementFeedbackCallback)
        #add Subscriber for camera data feedback
        rospy.spin()
