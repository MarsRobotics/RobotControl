from .state import State


class DriveToReturn(State):
    # init attributes of state
    def __init__(self):
        super().__init__("DriveToReturn", "Dump")
        self.transitionReady = False

    # implementation for each state: overridden
    def run(self, moveInstructions):
        print("\n>run() not implemented\n")

        # always begin with no transition
        self.transitionReady = False

        # reverse and spin
        # L or R depending on side of beacon
        # cannot see side beacon
        # main beacon must be specified size.
        # needs to be procedure to "parallel park" and try again if criteria not met
        # ^^ perhaps make the above the dock state

        self.transitionReady = True

    # implementation for each state: overridden
    def transition(self):
        return self.transitionReady