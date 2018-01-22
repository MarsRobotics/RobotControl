class State():
    #init attributes of state
    def __init__(self, name, nextState):
        self.name = name
        self.nextState = nextState

    #implementation for each state: overridden
    def run(self):
        print(self.name)
        print("\n>run() not implemented\n")

    def setNextState(self, name):
        self.nextState = name
    
    def getNextState(self):
        return self.nextState

