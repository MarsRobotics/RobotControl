from command2ros.src.stateMachine.states.State import State
from command2ros.src.MovementData import MovementData


class DriveToDigState(State):
    # init attributes of state
    def __init__(self):
        super().__init__("DriveToDig", "Dig")
        self.moveCommand = MovementData()

    # implementation for each state: overridden
    def run(self,cr, moveID):
        self.moveCommand.serialID = moveID
        cr.setCommand(self.moveCommand)

        # drive foward until beacon is x pixels or portion of screen
        # must be able to see front beacon
        print("send command")
        cr.sendMovementCommand('move')
        return (moveID)

