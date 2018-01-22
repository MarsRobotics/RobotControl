from states.state import State

class MoveState(State):
    #init attributes of state
    def __init__(self):
        super().__init__("Move", "Scan")

    #implementation for each state: overridden
    def run(self):
        print("\n>run() not implemented\n")