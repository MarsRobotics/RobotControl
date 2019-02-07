from states.startState import StartState
from states.driveToDigState import driveToDigState
from states.driveToReturnState import driveToReturnState
from states.digState import DigState
from states.dumpState import DumpState

#track current state and program
class StateMachine():

    #init robot
    def __init__(self):
        #init all states
        self.startState = StartState()
        #self.scanDigState = ScanDigState()
        #self.scanDumpState = ScanDumpState()
        #self.moveDigState = MoveDigState()
        #self.moveDumpState = MoveDumpState()
        self.driveToDigState = DriveToDigState()
        self.digState = DigState()
        self.driveToReturnState = DriveToReturnState()
        self.dumpState = DumpState()
        # 

        #set current state
        self.currentState = self.startState

        #whether or not to go dig, determines which scan state to use
        self.dig = True

    #control program
    def main(self):
        print("\n>Starting Main\n")


#PROGRAM ENTRY
if __name__ == "__main__":
    sm = StateMachine()
    sm.main()
#two seperate states for scan, dig and dump
#no separate transition.py, each state determines transition
