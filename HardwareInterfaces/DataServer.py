import sys
sys.path.append("/home/pi/ros_catkin_ws/src/command2ros/src")
import rospy
import roslib
import time
import socket
import threading

from MovementData import MovementData, MovementControlData
from DataTransferProtocol import receiveData, sendData
from command2ros.msg import MovementCommand

roslib.load_manifest('command2ros')

sendRate = 10 #Hz

"""
DataDistributor     Create threads to control network connections
                    from clients
"""
class DataDistributor(threading.Thread):

    def __init__(self):
        self.data = RobotData()
        threading.Thread.__init__(self)
        return

    #set up socket to receive incoming requests
    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverAddress = ("192.168.1.45", 10000) #George
        s.bind(serverAddress)
        s.listen(1) #backlog is 1

        #accept connections and spawn thread to handle
        #until server closes
        while True:
            clientSocket, address = s.accept()
            cs = DataServer(clientSocket, self, address)
            cs.run()
        return

"""
DataServer      Manage connection to a given client, receives and
                sends commands
"""
class DataServer(threading.Thread):

    def __init__(self, socket, distributor, address):
        self.socket = socket
        self.distributor = distributor #George
        self.address = address         

        threading.Thread.__init__(self)
        return

    def run(self):
        try:
            sendTime = 0

            while True:
                self.socket.setblocking(1)

                #send data to the client if time has passed
                if sendTime < time.time():
                    sendData(self.socket, self.distributor.data)
                    sendTime = time.time() + 1/float(sendRate)

                try:
                    self.socket.setblocking(0)

                    #get new command
                    newCommand = receiveData(self.socket)

                    #add command to execution queue
                    if newCommand.eStop:
                        commandQueue.insert(0, newCommand)
                    else:
                        commandQueue.append(newCommand)
                except socket.error:
                    continue
        except socket.error: 
            #lost connection, stop robot
            newCommand = MovementControlData()
            newCommand.eStop = True
            commandQueue.insert(0, newCommand)
            return
        return

#queue for sending movement commands to motors
commandQueue = []

#handles connections between clients
dataDist = DataDistributor()
dataDist.start()

#create ros publisher to update/send data
pub = rospy.Publisher('MovementCommand', queue_size=10)
rospy.init_node('command2ros', anonymous=True)

#publish commands to arduino
while True:
    if len(commandQueue) > 0:
        command = commandQueue.pop(0)

        #update to the next command
        mc = MovementCommand()
        mc.driveDist = command.driveDist #distance to drive meters  
        mc.turn = command.turn           #degrees for articulation motors
        mc.packout = command.packout     #starting sequence, wheels roll out
        mc.packin = command.packin       #ending sequence, wheels tucked under
        mc.eStop = command.eStop         #stop robot TODO:eStop and stop?
        pub.publish(mc)