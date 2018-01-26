from states.state import State

class DumpState(State):
    #init attributes of state
    def __init__(self):
        super().__init__("Dump", "ScanDig")
        self.transitionReady = False

    #implementation for each state: overridden
    def run(self):
        print("\n>run() not implemented\n")
        
        #always begin with no transition
        self.transitionReady = False

        #dump material

        self.transitionReady = True

    #implementation for each state: overridden
    def transition(self):
        return self.transitionReady