from states.state import State

class MoveDumpState(State):
    #init attributes of state
    def __init__(self):
        super().__init__("MoveDump", "ScanDump")
        self.transitionReady = False

    #implementation for each state: overridden
    def run(self, moveInstructions):
        print("\n>run() not implemented\n")
        
        #always begin with no transition
        self.transitionReady = False

        #execute move instructions        

        self.transitionReady = True

    #implementation for each state: overridden
    def transition(self):
        return self.transitionReady