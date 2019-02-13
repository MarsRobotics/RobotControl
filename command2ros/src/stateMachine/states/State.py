class State:

    #init attributes of state
    def __init__(self, name, nextState):
        self.name = name
        self.nextState = nextState

    #implementation for each state: overridden
    def run(self, cr, moveID):
        print(self.name)
