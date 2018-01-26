from states.state import State

class ScanDumpState(State):
    #init attributes of state
    def __init__(self):
        super().__init__("ScanDump", "ScanDig")

    #implementation for each state: overridden
    def run(self):
        print("\n>run() not implemented\n")