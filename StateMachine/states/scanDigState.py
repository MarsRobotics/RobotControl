from states.state import State

class ScanDigState(State):
    #init attributes of state
    def __init__(self):
        super().__init__("ScanDig", "ScanDig")

    #implementation for each state: overridden
    def run(self):
        print("\n>run() not implemented\n")