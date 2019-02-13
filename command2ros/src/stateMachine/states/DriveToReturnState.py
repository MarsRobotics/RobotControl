from command2ros.src.stateMachine.states.State import State
from command2ros.src.MovementData import MovementData

class DriveToReturnState(State):
    # init attributes of state
    def __init__(self):
        super().__init__("DriveToReturn", "Dump")

    # implementation for each state: overridden
    def run(self, cr, moveID):
        c = MovementData()
        c.SerialID = moveID
        cr.setMoveCommand(c)
        cr.sendMovementCommand('move')
        return(moveID)

        # reverse and spin
        # L or R depending on side of beacon
        # cannot see side beacon
        # main beacon must be specified size.
        # needs to be procedure to "parallel park" and try again if criteria not met
        # ^^ perhaps make the above the dock state
