from command2ros.src.stateMachine.states import State
from command2ros.src.DumpData import DumpData

class DumpState(State):
    #init attributes of state
    def __init__(self):
        super().__init__("Dump", "Start")

    #implementation for each state: overridden
    def run(self, cr, moveID):
        dumpData = DumpData()
        dumpData.serialID = moveID
        dumpData.beltDirection = 1
        dumpData.speed = 2
        cr.setDumpCommand(dumpData)
        cr.sendCommand('dump')

        return(moveID)