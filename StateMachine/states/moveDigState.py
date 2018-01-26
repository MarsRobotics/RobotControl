from states.state import State

class MoveDigState(State):
    #init attributes of state
    def __init__(self):
        super().__init__("MoveDig", "ScanDig")
        self.transitionReady = False
        self.digSiteDistance = 0

    #implementation for each state: overridden
    def run(self, moveInstructions):
        print("\n>run() not implemented\n")
        
        #always begin with no transition
        self.transitionReady = False

        #track distance
        #execute move instructions        
        #when in dig site then
        self.transitionReady = True

    #implementation for each state: overridden
    def transition(self):
        return self.transitionReady