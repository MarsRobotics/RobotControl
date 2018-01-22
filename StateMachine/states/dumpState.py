from states.state import State

class DumpState(State):
    #init attributes of state
    def __init__(self):
        super().__init__("Dump", "Scan")

    #implementation for each state: overridden
    def run(self):
        print("\n>run() not implemented\n")