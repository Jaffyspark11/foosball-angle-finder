import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider
from skimage.draw import line

class Table:

    def __init__(self):
        self.wall = 40
        self.length = int(46 * 16 + 2*self.wall)
        self.width = int(26.75 * 16 + 2*self.wall)
        self.goal = int(6.875 * 16)
        self.backWallLength = ((self.width - self.goal) / 2)
        self.goalRange = (int(self.backWallLength), int(self.backWallLength + self.goal))
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

        for i in range(0, int(self.goalRange[0])):
            table[i, 0:40] = 3
            table[i, -40:] = 3


        for i in range(int(self.goalRange[0]), int(self.goalRange[1])):
            table[i, 0:40] = 9
            table[i, -40:] = 9

        for i in range(int(self.goalRange[1]), int(self.width)):
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
        
        #add Ball

        ballPositionY = ((self.width - self.ballDiameter) / 2)
        ballPositionX = ((self.length - self.ballDiameter) / 2)

        ballY = (int(ballPositionY), int(ballPositionY + self.ballDiameter))
        ballX = (int(ballPositionX), int(ballPositionX + self.ballDiameter))

        for i in range(ballY[0], ballY[1]):

            table[i, ballX[0]:ballX[1]] = 8

        return table
    

    def find_valid_angles(self, ballPosition):
        valid_angles = []

        ball_x, ball_y = ballPosition
        ball_diameter = self.ballDiameter

        for i in range(int(table.goalRange[0]), int(table.goalRange[1]), 8):
            
            x = [ball_x, 775]
            y = [ball_y, i]

            rr, cc = line(y[0], x[0], y[1], x[1])

            intersects = False
            for r, c in zip(rr, cc):
                # Check if any point within the ball diameter intersects with a player piece
                for dr in range(-ball_diameter // 2, ball_diameter // 2 + 1):
                    for dc in range(-ball_diameter // 2, ball_diameter // 2 + 1):
                        if matrix[r + dr, c + dc] == 7:
                            intersects = True
                            break
                    if intersects:
                        break
                if intersects:
                    break
            
            if not intersects:
                # Iterate through each point of the line and plot it
                valid_angles.append((rr, cc))
                for r, c in zip(rr, cc):
                    plt.plot(c, r, color="white", marker='.', markersize=1)
            
        return valid_angles



# Instantiate the Table class
table = Table()

# Build the foosball table matrix
matrix = table.buildTable()

# Plot the foosball table
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)
plt.imshow(matrix, cmap='viridis')

# Initial ball position
ball_x_initial = 550
ball_y_initial = 140

# Plot the initial ball position
ball_plot, = plt.plot(ball_x_initial, ball_y_initial, 'ro')

# Slider for adjusting ball position
ax_ball_position = plt.axes([0.25, 0.1, 0.65, 0.03])
slider_ball_position = Slider(ax_ball_position, 'Ball Position', 40, table.width - 40, valinit=ball_y_initial)

# Button for updating valid angles
ax_button = plt.axes([0.8, 0.025, 0.1, 0.04])
button_update = Button(ax_button, 'Update')

def update(val):
    ball_y = int(val)
    ball_x = ball_x_initial
    
    # Plot the updated ball position
    ball_plot.set_data(ball_x, ball_y)
    fig.canvas.draw_idle()

def on_button_press(event):
    ball_y = int(slider_ball_position.val)
    ball_x = ball_x_initial

    # Clear previous ball position plot
    ball_plot.set_data([], [])

    # Find valid angles for the updated ball position
    valid_angles = table.find_valid_angles((ball_x, ball_y))

    # Plot the valid angles
    for rr, cc in valid_angles:
        for r, c in zip(rr, cc):
            plt.plot(c, r, color="white", marker='.', markersize=1)
    
    # Plot the updated ball position
    ball_plot.set_data(ball_x, ball_y)
    fig.canvas.draw_idle()

# Register the update function to the slider
slider_ball_position.on_changed(update)

# Register the button press function to the button
button_update.on_clicked(on_button_press)

plt.show()