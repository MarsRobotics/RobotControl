from states.startState import StartState
from states.scanState import ScanState
from states.moveState import MoveState
from states.digState import DigState
from states.dumpState import DumpState

#track current state and program
class StateMachine():

    #init robot
    def __init__(self): 
        #init all states       
        self.startState = StartState()
        self.scanState = ScanState()
        self.moveState = MoveState()
        self.dumpState = DumpState()
        self.digState = DigState()

        #set current state
        self.currentState = self.startState

    #control program
    def main(self):
        print("\n>main() not implemented\n")

#PROGRAM ENTRY
if __name__ == "__main__":
    sm = StateMachine()
    sm.main()
