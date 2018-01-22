from states.state import State

class ScanState(State):
    #init attributes of state
    def __init__(self):
        super().__init__("Scan", "Scan")

    #implementation for each state: overridden
    def run(self):
        print("\n>run() not implemented\n")