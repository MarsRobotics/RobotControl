from states.state import State

class StartState(State):
    #init attributes of state
    def __init__(self):
        super().__init__("Start", "Scan")

    #implementation for each state: overridden
    def run(self):
        print("\n>run() not implemented\n")
