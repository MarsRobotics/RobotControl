#!/usr/bin/env python3

import rospy
import command2ros.msg.MovementFeedback as MovementFeedback
import command2ros.msg.ImageProc as ImageProc
import command2ros.msg.MovementFeedbackData as MovementFeedbackData
import command2ros.msg.ImageProcData as ImageProcData
import threading

class FeedbackHandler(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.movementFBmessageQueue = []
        self.imageProcmessageQueue = []
        return

    def run(self):
        self.listener()

    def movementFeedbackCallback(self, data):
        feedback = MovementFeedbackData()
        feedback.ready = data.ready
        feedback.messageID = data.messageID
        feedback.serialID = data.serialID
        feedback.msg = data.msg
        self.movementFBmessageQueue.append(feedback)

    def imageProcCallback(self, data):
        imageData = ImageProcData()
        imageData.serialID = 0

        imageData.xCoordMainBeaconCenter = data.xCoordMainBeaconCenter
        imageData.yCoordMainBeaconCenter = data.yCoordMainBeaconCenter
        imageData.xCoordMainBeaconLB = data.xCoordMainBeaconLB
        imageData.yCoordMainBeaconLB = data.yCoordMainBeaconLB
        imageData.xCoordMainBeaconUB = data.xCoordMainBeaconUP
        imageData.yCoordMainBeaconUB = data.yCoordMainBeaconUP

        imageData.xCoordSternBeaconCenter = data.xCoordSternBeaconCenter
        imageData.yCoordSternBeaconCenter = data.yCordSternBeaconCenter
        imageData.xCoordSternBeaconLB = data.xCoordSternBeaconLB
        imageData.yCoordSternBeaconLB = data.yCoordSternBeaconLB
        imageData.xCoordSternBeaconUB = data.xCoordSternBeaconUP
        imageData.yCoordSternBeaconUB = data.yCoordSternBeaconUP

        imageData.xCoordBowBeaconCenter = data.xCoordBowBeaconCenter
        imageData.yCoordBowBeaconCenter = data.yCoordBowBeaconCenter
        imageData.xCoordBowBeaconLB = data.xCoordBowBeaconLB
        imageData.yCoordBowBeaconLB = data.yCoordBowBeaconLB
        imageData.xCoordBowBeaconUB = data.xCoordBowBeaconUP
        imageData.yCoordBowBeaconUB = data.yCoordBowBeaconUP

        imageData.xCoordFrontBeaconCenter = data.xCoordFrontBeaconCenter
        imageData.yCoordFrontBeaconCenter = data.yCoordFrontBeaconCenter
        imageData.xCoordFrontBeaconLB = data.xCoordFrontBeaconLB
        imageData.yCoordFrontBeaconLB = data.yCoordFrontBeaconLB
        imageData.xCoordFrontBeaconUB = data.xCoordFrontBeaconUP
        imageData.yCoordFrontBeaconUB = data.yCoordFrontBeaconUP

        self.imageProcmessageQueue.append(imageData)

    def listener(self):
        rospy.Subscriber("MovementFeedback", MovementFeedback, self.movementFeedbackCallback)
        rospy.Subscriber("ImageProc", ImageProc, self.imageProcCallback)
        rospy.spin()
