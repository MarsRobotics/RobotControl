class State():
    #init attributes of state
    def __init__(self, name, nextState):
        self.name = name
        self.nextState = nextState
        self.transitionReady = False

    #implementation for each state: overridden
    def run(self):
        print(self.name)
        print("\n>run() not implemented\n")

    #implementation for each state: overridden
    def transition(self):
        return False

