from states.state import State

class ScanDigState(State):
    #init attributes of state
    def __init__(self):
        super().__init__("ScanDig", "Move")
        self.transitionReady = False

    #implementation for each state: overridden
    def run(self):
        print("\n>run() not implemented\n")

        #always begin with no transition
        self.transitionReady = False

        #thoughts: three threads- produce, consume, send data from LiDAR
        #use modified old code, for basics of plan see comments directly below

        #scan with LiDAR

        #A: create map for laptop
        #A: send map to laptop
        #A: receive move instructions from laptop

        #B: create map for AI
        #B: interpret map for AI & get move instructions

        self.transitionReady = True #change later to signal move instruction set is ready

    #implementation for each state: overridden
    def transition(self):
        return self.transitionReady