from .state import State


class DriveToDig(State):
    # init attributes of state
    def __init__(self):
        super().__init__("DriveToDig", "Dig")
        self.transitionReady = False

    # implementation for each state: overridden
    def run(self, moveInstructions):
        print("\n>run() not implemented\n")

        # always begin with no transition
        self.transitionReady = False

        # drive foward until beacon is x pixels or portion of screen
        # must be able to see front beacon

        self.transitionReady = True

    # implementation for each state: overridden
    def transition(self):
        return self.transitionReady