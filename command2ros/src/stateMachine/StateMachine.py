#!/usr/bin/env python3
import time
import sys
sys.path.append("/home/pi/ros_catkin_ws/src/command2ros/src/stateMachine/")

import rospy
import roslib
roslib.load_manifest('command2ros')

import command2ros.msg.DigCommand as DigCommand
import command2ros.msg.DumpCommand as DumpCommand
import command2ros.msg.MovementCommand as MovementCommand
import command2ros.msg.MovementFeedback as MovementFeedback
import command2ros.msg.ImageProc as ImageProc

from .states.StartState import StartState
from .states.DriveToDigState import DriveToDigState
from .states.DriveToReturnState import DriveToReturnState
from .states.DigState import DigState
from .states.DumpState import DumpState
from .states.DriveToDigState import DriveToDigState
from .states.DriveToReturnState import DriveToReturnState
from .states.ManualMoveState import ManualMoveState

from command2ros.src.DataServer import DataDistributor
from command2ros.src.CommandRobot import CommandRobot
from command2ros.src.FeedbackHandler import FeedbackHandler

#track current state and program
class StateMachine():

    #init robot
    def __init__(self):
        self.manual = True

        #init all states
        self.startState = StartState()
        self.driveToDigState = DriveToDigState()
        self.digState = DigState()
        self.driveToReturnState = DriveToReturnState()
        self.dumpState = DumpState()

        self.ManualMoveState = ManualMoveState()


        #set current state
        if self.manual:
            self.currentState = self.ManualMoveState
        else:
            self.currentState = self.startState

    #control program
    def startRobot(self):
        end = False
        moveID = 1
        print("robot is starting")
        movementPub, digPub, dumpPub = self.rosSetup()
        print("ros has been set up")
        feedbackHandler = FeedbackHandler()
        feedbackHandler.start()
        print("feedback handler set up")
        movementDataDistributer = self.dataDistributorSetup(movementPub, 'move')
        digDataDistributer = self.dataDistributorSetup(digPub, 'dig')
        dumpDataDistributer = self.dataDistributorSetup(dumpPub,'dump')
        print("data distributors to send commands set up")

        # use to update the next command and send to arduino mega
        cr = CommandRobot()

        if self.currentState.name == "ManualMoveState":
            print("Starting in manual command mode")

            while (True):
                moveID = self.currentState.run(cr, moveID)

                if self.currentState.autonomousMode:
                    print("switching from manual mode to autonomous mode")
                    self.currentState = self.StartState
                    break
                elif self.currentState.endProgram:
                    end = True
                    print("ending the program")
                    break

        if self.currentState.name == "StartState":
            moveID = self.currentState.run(cr, moveID)

            #set the current state to the specified next state
            next = self.currentState.nextState
            self.setNext(next) 

        while not end:            
            print("Run " + self.currentState.name)
            moveID = self.currentState.run(cr, moveID)

            #set the current state to the specified next state
            next = self.currentState.nextState
            self.setNext(next) 

        if end:
            # dd.join()
            # print("data distributor stopped")
            time.sleep(2)
            exit()
        return

        # set next state

    def setNext(self, next):
        if next == self.StartState.name:
            self.currentState = self.DriveToDigState
        elif next == self.DriveToDigState.name:
            self.currentState = self.DigState
        elif next == self.DigState.name:
            self.currentState = self.DriveToReturnState
        elif next == self.DriveToReturnStae.name:
            self.currentState = self.DumpState
        elif next == self.DumpState.name:
            self.currentState = self.StartState

    # create distributor and server for movement commands
    def dataDistributorSetup(self, pub):
        # handles connection to client to receive commands
        dataDist = DataDistributor(pub)
        dataDist.start()
        return dataDist

    # ros node for program and publisher for movement commands
    def rosSetup(self):
        # create ros publisher to update/send data
        movementPub = rospy.Publisher('MovementCommand', MovementCommand, queue_size=10)
        digPub = rospy.Publisher('DigCommand', DigCommand, queue_size=10)
        dumpPub = rospy.Publisher('DumpCommand', DumpCommand, queue_size=10)
        rospy.init_node('command2ros', anonymous=True)

        return (movementPub, digPub, dumpPub)


# PROGRAM ENTRY
if __name__ == "__main__":

    sm = StateMachine()
    sm.startRobot()
