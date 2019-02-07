from .state import State

class DigState(State):
    #init attributes of state
    def __init__(self):
        super().__init__("Dig", "DriveToReturn")
        self.transitionReady = False

    #implementation for each state: overridden
    def run(self):
        print("\n>run() not implemented\n")
        #always begin with no transition
        self.transitionReady = False

        # lower/dig action with stepper motor
        # monitor sensors to tell if "stuck"
        # load sensor (?) to tell if "full" or time reached
        # raise digger

        
        self.transitionReady = True

    #implementation for each state: overridden
    def transition(self):
        return self.transitionReady