#!/usr/bin/env python3
# cPickle is faster
try:
    import cPickle as pickle
except ImportError:
    import pickle

import time
import socket
from socket import error as socketError
from MovementData import MovementData
from DigData import DigData
from DumpData import DumpData
from DataTransferProtocol import receiveData, sendData

BODY_SIZE_STRING_SIZE = 10

"""
CommandRobot    Send robot movement commands (MovementCommand msg) to Arduino
"""


class CommandRobot:

    def __init__(self):
        self.HOST = "127.0.0.1"
        self.PORT = 10000
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.HOST, self.PORT))
        self.sock = s
        self.lastData = MovementData()
        self.currentData = MovementData()
        self.lastDigData = DigData()
        self.currentDigData = DigData()
        self.lastDumpData = DumpData()
        self.currentDumpData = DumpData()
        return

    def stop(self):
        self.sock.shutdown(socket.SHUT_RDWR)
        self.sock.close()
        print("command robot is closed")

    # communication with the DataDistributor
    def sendCommand(self, data):
        # send new command data
        if (data == 'move'):
            sendData(self.sock, self.currentData)
        if (data == 'dig'):
            sendData(self.sock, self.currentDigData)
        if (data =='dump'):
            sendData(self.sock, self.currentDumpData)
        time.sleep(2)
        if self.currentData.endProgram:
            self.sock.shutdown(socket.SHUT_RDWR)
            self.sock.close()
            print("command robot is closed")

    # assign a new command for the robot
    def setMovmentCommand(self, command):
        self.currentData.driveDirection = command.driveDirection
        self.currentData.packin = command.packin
        self.currentData.packout = command.packout
        self.currentData.stop = command.stop
        self.currentData.pause = command.pause
        self.currentData.serialID = command.serialID

    def setDigCommand(self, command):
        self.digData.serialID = command.serialID
        self.digData.digDirection = command.digDirection
        self.digData.stop = command.stop


    def setDumpCommand(self, command):
        self.dumpData.serialID = command.serialID
        self.dumpData.beltDirection = command.digDirection
        self.dumpData.speed = command.speed
        self.dumpData.stop = command.stop


