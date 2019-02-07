from .state import State

class StartState(State):
    #init attributes of state
    def __init__(self):
        super().__init__("Start", "DriveToDig")
        self.transitionReady = False

    #implementation for each state: overridden
    def run(self):
        print("\n>run() not implemented, psuedocode below\n")

        #always begin with no transition
        self.transitionReady = False

        # self.pack_out (or similar) but return here
        #
        #
        #TO IMPLEMENT:

        # conntinually get image , pixel count and location of beacon:  x1 deg < beacon < x2 deg

        #
        # mainBeacon:
        #  [        ]|||||||||||||||||[        ]
        #    stern                       bow
        #
        #  0* corresponds to center front (side with digger) of bot
        #  90* ==> center right
        #  180* ==> center back
        #  270* ==> center left
        #
        #        BACK                     180*
        #
        #  RIGHT       LEFT   ==>    90*       270*
        #
        #        FRONT                     0*
        #

        # start state sub state machine
        #LB - >lower bound
        #UP -> upper bound:
        frontLB = 315
        front = 0
        front_alt = 360
        frontUP = 45
        # RIGHT
        rightLB = 45
        right = 90
        rightUP = 135

        backLB = 135
        back = 180
        backUP = 225

        leftLB = 225
        left = 270
        leftUP = 315

        subStartStateTransitionReady = False

        # 'get' (or look at most recent) image data packet
        # packet should contain: mainBeaconLB, mainBeaconUP , mainBeaconCenter, sternBeaconLB, sternBeaconUP, sternBeaconCenter
        mainBeaconLB =  0;#packet.get(mainBeaconLB)
        mainBeaconUP = 0;
        mainBeaconCenter =0;
        sternBeaconLB = 0;
        sternBeaconUP = 0;
        sternBeaconCenter = 0;


        while not subStartStateTransitionReady:
            if mainBeaconCenter > frontLB or mainBeaconCenter < frontUP:
                if front < sternBeaconCenter < right:
                    #turn left
                elif left < sternBeaconCenter  < front_alt:
                    # turn right

            elif leftLB < mainBeaconCenter  < leftUP:
                if back < sternBeaconCenter < left:
                    subStartStateTransitionReady = True
                elif left < sternBeaconCenter < front_alt:
                    #turn right

            elif backLB < mainBeaconCenter < backUP:
                if back < sternBeaconCenter < left:
                    #turn right
                elif  right < sternBeaconCenter < back:
                    #turn left
            elif rightLB < mainBeaconCenter < rightUP:
                if right < sternBeaconCenter < back:
                    subStartStateTransitionReady = True
                elif front < sternBeaconCenter < right:
                    #turn left


        self.transitionReady = True


    #implementation for each state: overridden
    def transition(self):
        return self.transitionReady
