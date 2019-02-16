import matplotlib

matplotlib.use("agg")
from command2ros.src.stateMachine.states.State import State
from command2ros.src.DataTransferProtocol import receiveData, sendData
from command2ros.src.MovementData import MovementData
from manual.ManualData import ManualData
import socket
import time
import matplotlib.pyplot as plt


# Manual Move State (preserved from 2018 competition) to manually control the robot from laptop

class ManualMoveState(State):
    # init attributes of state
    def __init__(self):
        super().__init__("ManualMoveState", "ManualMoveState")
        self.HOST = "10.0.0.77"  # laptop IP
        self.PORT = 20000  # communication port

        # connect to laptop (note: laptop program is server so must start laptop program first)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("attempt to connect manual")
        s.connect((self.HOST, self.PORT))
        print("connected manual")
        self.sock = s
        self.autonomousMode = False
        self.endProgram = False
        self.pub = None  # publisher for the Scan topic
        return

    '''
    Run for ManualMoveState:    Receive manual commands to direct robot from a laptop

    cr      CommandRobot allows commands to be published to the Mega
    scanID  ID number for the message to be published to the Scan topic
    moveID  ID number for the message to be published to the MovementCommand topic
    '''

    #TODO fix implementation to make consistent
    def run(self, movementPub, digPub, moveID):
        try:
            self.sock.setblocking(1)
            manualCommand = receiveData(self.sock)
            print("received new command")

            # shut down the robot
            if manualCommand.endProgram:
                c = MovementData()
                c.manual = True
                c.endProgram = manualCommand.endProgram
                # cr.setCommand(c)
                # cr.sendCommand()
                movementPub.publish(
                    serialID=c.serialID,
                    driveDirection=c.driveDirection,
                    stop=c.stop,
                    packin=c.packin,
                    packOut=c.packOut,
                    pause=c.pause,
                    msg=c.msg)
                print("send command to end program")
                time.sleep(2)
                self.endProgram = True
                self.sock.shutdown(socket.SHUT_RDWR)
                self.sock.close()
                print("manual state closed by end program")
            # switch to autonomous mode
            elif manualCommand.autonomousMode:
                self.autonomousMode = True
                self.sock.shutdown(socket.SHUT_RDWR)
                self.sock.close()
                print("manual state closed by switch to autonomous")
            # scan LiDAR

            else:
                c = MovementData()
                c.serailID= moveID
                c.driveDirection = manualCommand.driveDirection
                c.stop = manualCommand.stop
                c.packin = manualCommand.packin
                c.packout = manualCommand.packout
                c.pause = manualCommand.pause
                c.msg = manualCommand.msg
                moveID += 1

                # cr.setCommand(c)
                # print("send movement command to robot")
                # cr.sendCommand()
                movementPub.publish(
                    serialID=c.serialID,
                    driveDirection=c.driveDirection,
                    stop=c.stop,
                    packin=c.packin,
                    packOut=c.packOut,
                    pause=c.pause,
                    msg=c.msg)

                # digPub.publish(manualCommand.raiseForDig)
        # socket was shut down unexpectedly, shut down robot
        except socket.error:
            c = MovementData()
            c.endProgram = True
            # cr.setCommand(c)
            # cr.sendCommand()
            movementPub.publish(
                serialID=c.serialID,
                driveDirection=c.driveDirection,
                stop=c.stop,
                packin=c.packin,
                packOut=c.packOut,
                pause=c.pause,
                msg=c.msg)
            print("send command to end program")
            time.sleep(2)
            self.endProgram = True
            self.sock.shutdown(socket.SHUT_RDWR)
            self.sock.close()
            print("manual state closed")
            print("Socket error manual command")

        return (moveID)

        # keep publisher for Scan topic

    def setPub(self, publisher):
        self.pub = publisher

    def view(self, z, distance):
        plt.pcolormesh([z, distance])  # Figure out how this works! Also, why z and dist
        plt.colorbar()  # need a colorbar to show the intensity scale
        plt.show()
