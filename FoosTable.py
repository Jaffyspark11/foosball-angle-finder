import numpy as np
import matplotlib.pyplot as plt

class Table:

    def __init__(self):
        self.wall = 40
        self.length = int(46 * 16 + 2*self.wall)
        self.width = int(26.75 * 16 + 2*self.wall)
        self.goal = int(6.875 * 16)
        self.polegap = int(5 * 16)
        self.oneManGap = int(2.875 * 16 + self.wall)
        self.pieceWidth = int(0.75 * 16)
        self.pieceDepth = int(0.5 * 16)
        self.ballDiameter = int(1.25 * 16)
        self.poleWidth = int(0.625 * 16)
        self.stopper = int(1*16)
        self.fiveManGap = int(3.875 * 16)
        self.threeManGap = int(6.25 * 16)
        self.twoManGap = int(8.5 * 16)
        self.oneManStopperGap = int(7 * 16)
        self.fiveMen = [
            [self.stopper + self.wall, self.stopper + self.wall + self.pieceWidth],
            [self.stopper + self.wall + self.pieceWidth + self.fiveManGap, self.stopper + self.wall + 2 * self.pieceWidth + self.fiveManGap],
            [self.stopper + self.wall + 2 * (self.pieceWidth + self.fiveManGap), self.stopper + self.wall + self.pieceWidth + 2 * (self.fiveManGap + self.pieceWidth)],
            [self.stopper + self.wall + 3 * (self.pieceWidth + self.fiveManGap), self.stopper + self.wall + self.pieceWidth + 3 * (self.fiveManGap + self.pieceWidth)],
            [self.stopper + self.wall + 4 * (self.pieceWidth + self.fiveManGap), self.stopper + self.wall + self.pieceWidth + 4 * (self.fiveManGap + self.pieceWidth)],
        ]
        self.threeMen = [
            [self.stopper + self.wall, self.stopper + self.wall + self.pieceWidth],
            [self.stopper + self.wall + self.pieceWidth + self.threeManGap, self.stopper + self.wall + 2 * self.pieceWidth + self.threeManGap],
            [self.stopper + self.wall + 2 * (self.pieceWidth + self.threeManGap), self.stopper + self.wall + self.pieceWidth + 2 * (self.threeManGap + self.pieceWidth)]
        ]
        self.twoMen = [
            [self.stopper + self.wall, self.stopper + self.wall + self.pieceWidth],
            [self.stopper + self.wall + self.pieceWidth + self.twoManGap, self.stopper + self.wall + 2 * self.pieceWidth + self.twoManGap]
        ]
        self.oneMan = [
            int(self.stopper + self.wall + self.oneManStopperGap),
            int(self.stopper + self.wall + self.oneManStopperGap + self.pieceWidth)
        ]


    ##### Matrix Definitions
        
        #Goal = 9
        #Player = 7
        #Ball = 8
        #Wall = 3
        #pole = 4
        #blocker = 2

    def buildTable(self):

        table = np.zeros((int(self.width), int(self.length)))

        ###Add walls and Goals to either side

        backWallLength = ((self.width - self.goal) / 2)

        goalRange = (int(backWallLength), int(backWallLength + self.goal))

        for i in range(0, int(goalRange[0])):
            table[i, 0:40] = 3
            table[i, -40:] = 3


        for i in range(int(goalRange[0]), int(goalRange[1])):
            table[i, 0:40] = 9
            table[i, -40:] = 9

        for i in range(int(goalRange[1]), int(self.width)):
            table[i, 0:40] = 3
            table[i, -40:] = 3

        ###Add Poles and players
            
        poleRanges = [
            [self.oneManGap, self.oneManGap + self.poleWidth],
            [self.oneManGap + self.poleWidth + self.polegap, self.oneManGap + self.poleWidth + self.polegap + self.poleWidth],
            [self.oneManGap + 2 * (self.poleWidth + self.polegap), self.oneManGap + self.poleWidth + 2 * (self.polegap + self.poleWidth)],
            [self.oneManGap + 3 * (self.poleWidth + self.polegap), self.oneManGap + self.poleWidth + 3 * (self.polegap + self.poleWidth)],
            [self.oneManGap + 4 * (self.poleWidth + self.polegap), self.oneManGap + self.poleWidth + 4 * (self.polegap + self.poleWidth)],
            [self.oneManGap + 5 * (self.poleWidth + self.polegap), self.oneManGap + self.poleWidth + 5 * (self.polegap + self.poleWidth)],
            [self.oneManGap + 6 * (self.poleWidth + self.polegap), self.oneManGap + self.poleWidth + 6 * (self.polegap + self.poleWidth)],
            [self.oneManGap + 7 * (self.poleWidth + self.polegap), self.oneManGap + self.poleWidth + 7 * (self.polegap + self.poleWidth)],           
        ]
        
        print(poleRanges)
        
        for i in range(int(poleRanges[0][0]), int(poleRanges[0][1])):

            table[:, i] = 4

        for i in range(int(poleRanges[1][0]), int(poleRanges[1][1])):

            table[:, i] = 4

        for i in range(int(poleRanges[2][0]), int(poleRanges[2][1])):

            table[:, i] = 4

        for i in range(int(poleRanges[3][0]), int(poleRanges[3][1])):

            table[:, i] = 4

        for i in range(int(poleRanges[4][0]), int(poleRanges[4][1])):

            table[:, i] = 4

        for i in range(int(poleRanges[5][0]), int(poleRanges[5][1])):

            table[:, i] = 4

        for i in range(int(poleRanges[6][0]), int(poleRanges[6][1])):

            table[:, i] = 4

        for i in range(int(poleRanges[7][0]), int(poleRanges[7][1])):

            table[:, i] = 4

        ###Add side Walls
            
        for i in range(0, self.length):
            table[0:40, i] = 3
            table[-40:, i] = 3  

        ###Add five men
            
        for i in range(self.wall, self.wall + self.stopper):
            table[i, poleRanges[3][0]:poleRanges[3][1]] = 2
            table[i, poleRanges[4][0]:poleRanges[4][1]] = 2
            
        for i in range(int(self.fiveMen[0][0]), int(self.fiveMen[0][1])):

            table[i, poleRanges[3][0]:poleRanges[3][1]] = 7
            table[i, poleRanges[4][0]:poleRanges[4][1]] = 7

        for i in range(int(self.fiveMen[1][0]), int(self.fiveMen[1][1])):

            table[i, poleRanges[3][0]:poleRanges[3][1]] = 7
            table[i, poleRanges[4][0]:poleRanges[4][1]] = 7

        for i in range(int(self.fiveMen[2][0]), int(self.fiveMen[2][1])):

            table[i, poleRanges[3][0]:poleRanges[3][1]] = 7
            table[i, poleRanges[4][0]:poleRanges[4][1]] = 7

        for i in range(int(self.fiveMen[3][0]), int(self.fiveMen[3][1])):

            table[i, poleRanges[3][0]:poleRanges[3][1]] = 7
            table[i, poleRanges[4][0]:poleRanges[4][1]] = 7

        for i in range(int(self.fiveMen[4][0]), int(self.fiveMen[4][1])):

            table[i, poleRanges[3][0]:poleRanges[3][1]] = 7
            table[i, poleRanges[4][0]:poleRanges[4][1]] = 7

        for i in range(int(self.fiveMen[4][1]), int(self.fiveMen[4][1]) + self.stopper):
            table[i, poleRanges[3][0]:poleRanges[3][1]] = 2
            table[i, poleRanges[4][0]:poleRanges[4][1]] = 2

        #Add three men
            
        for i in range(self.wall, self.wall + self.stopper):
            table[i, poleRanges[2][0]:poleRanges[2][1]] = 2
            table[i, poleRanges[5][0]:poleRanges[5][1]] = 2
            
        for i in range(int(self.threeMen[0][0]), int(self.threeMen[0][1])):

            table[i, poleRanges[2][0]:poleRanges[2][1]] = 7
            table[i, poleRanges[5][0]:poleRanges[5][1]] = 7

        for i in range(int(self.threeMen[1][0]), int(self.threeMen[1][1])):

            table[i, poleRanges[2][0]:poleRanges[2][1]] = 7
            table[i, poleRanges[5][0]:poleRanges[5][1]] = 7

        for i in range(int(self.threeMen[2][0]), int(self.threeMen[2][1])):

            table[i, poleRanges[2][0]:poleRanges[2][1]] = 7
            table[i, poleRanges[5][0]:poleRanges[5][1]] = 7
        
        for i in range(int(self.threeMen[2][1]), int(self.threeMen[2][1]) + self.stopper):
            table[i, poleRanges[2][0]:poleRanges[2][1]] = 2
            table[i, poleRanges[5][0]:poleRanges[5][1]] = 2

        #Add two men
            
        for i in range(self.wall, self.wall + self.stopper):
            table[i, poleRanges[1][0]:poleRanges[1][1]] = 2
            table[i, poleRanges[6][0]:poleRanges[6][1]] = 2
            
        for i in range(int(self.twoMen[0][0]), int(self.twoMen[0][1])):

            table[i, poleRanges[1][0]:poleRanges[1][1]] = 7
            table[i, poleRanges[6][0]:poleRanges[6][1]] = 7

        for i in range(int(self.twoMen[1][0]), int(self.twoMen[1][1])):

            table[i, poleRanges[1][0]:poleRanges[1][1]] = 7
            table[i, poleRanges[6][0]:poleRanges[6][1]] = 7
        
        for i in range(int(self.twoMen[1][1]), int(self.twoMen[1][1]) + self.stopper):
            table[i, poleRanges[1][0]:poleRanges[1][1]] = 2
            table[i, poleRanges[6][0]:poleRanges[6][1]] = 2

        #add one men
            
        for i in range(self.wall, self.wall + self.stopper):
            table[i, poleRanges[0][0]:poleRanges[0][1]] = 2
            table[i, poleRanges[7][0]:poleRanges[7][1]] = 2
            
        for i in range(int(self.oneMan[0]), int(self.oneMan[1])):

            table[i, poleRanges[0][0]:poleRanges[0][1]] = 7
            table[i, poleRanges[7][0]:poleRanges[7][1]] = 7
        
        for i in range(int(self.oneMan[1] + self.oneManStopperGap), int(self.oneMan[1] + self.oneManStopperGap + self.stopper)):
            table[i, poleRanges[0][0]:poleRanges[0][1]] = 2
            table[i, poleRanges[7][0]:poleRanges[7][1]] = 2
        



        return table

table = Table()

build = table.buildTable()

plt.imshow(build, cmap='viridis')
plt.colorbar()
plt.show()

