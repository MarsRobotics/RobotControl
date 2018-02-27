"""
MovementData        Define movement for robot      
"""
class MovementData:
    
    def __init__(self):
        self.driveDist = 0      #distance to drive forward in meters
        self.turn = 0           #degrees to turn robot
        self.packout = False    #starting sequence, wheels tucked under to roll out
        self.packin = False     #ending sequence, wheels roll in so tucked under
        self.eStop = False      #stop robot
        return