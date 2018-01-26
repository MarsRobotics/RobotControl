from states.startState import StartState
from states.scanDigState import ScanDigState
from states.scanDumpState import ScanDumpState
from states.moveState import MoveState
from states.digState import DigState
from states.dumpState import DumpState

#track current state and program
class StateMachine():

    #init robot
    def __init__(self): 
        #init all states       
        self.startState = StartState()
        self.scanDigState = ScanDigState()
        self.scanDumpState = ScanDumpState()
        self.moveState = MoveState()
        self.dumpState = DumpState()
        self.digState = DigState()

        #set current state
        self.currentState = self.startState

        #whether or not to go dig, determines which scan state to use
        self.dig = True

    #control program
    def main(self):
        print("\n>main() not implemented\n")

#PROGRAM ENTRY
if __name__ == "__main__":
    sm = StateMachine()
    sm.main()
#two seperate states for scan, dig and dump
#no separate transition.py, each state determines transition