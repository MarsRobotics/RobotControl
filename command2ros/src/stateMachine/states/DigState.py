from command2ros.src.stateMachine.states.State import State
from command2ros.src.DigData import DigData

class DigState(State):
    #init attributes of state
    def __init__(self):
        super().__init__("Dig", "DriveToReturn")

    #implementation for each state: overridden
    def run(self, cr, moveID):
        digData = DigData()
        digData.serialID = moveID

        cr.setDigCommand(digData)
        cr.sendCommand('dig')

        # lower/dig action with stepper motor
        # monitor sensors to tell if "stuck"
        # load sensor (?) to tell if "full" or time reached
        # raise digger


        return(moveID)