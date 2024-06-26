import math
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
        self.poleRanges = [
            [self.oneManGap, self.oneManGap + self.poleWidth],
            [self.oneManGap + self.poleWidth + self.polegap, self.oneManGap + self.poleWidth + self.polegap + self.poleWidth],
            [self.oneManGap + 2 * (self.poleWidth + self.polegap), self.oneManGap + self.poleWidth + 2 * (self.polegap + self.poleWidth)],
            [self.oneManGap + 3 * (self.poleWidth + self.polegap), self.oneManGap + self.poleWidth + 3 * (self.polegap + self.poleWidth)],
            [self.oneManGap + 4 * (self.poleWidth + self.polegap), self.oneManGap + self.poleWidth + 4 * (self.polegap + self.poleWidth)],
            [self.oneManGap + 5 * (self.poleWidth + self.polegap), self.oneManGap + self.poleWidth + 5 * (self.polegap + self.poleWidth)],
            [self.oneManGap + 6 * (self.poleWidth + self.polegap), self.oneManGap + self.poleWidth + 6 * (self.polegap + self.poleWidth)],
            [self.oneManGap + 7 * (self.poleWidth + self.polegap), self.oneManGap + self.poleWidth + 7 * (self.polegap + self.poleWidth)],           
        ]


    ##### Matrix Definitions
        
        #Goal = 9
        #Player = 7
        #Ball = 8
        #Wall = 3
        #pole = 4
        #blocker = 2



    def addP1OneMan(self, table, displacement=0):

        for i in range(self.wall + displacement, self.wall + self.stopper + displacement):
            table[i, self.poleRanges[0][0]:self.poleRanges[0][1]] = 2
            
        for i in range(int(self.oneMan[0] + displacement), int(self.oneMan[1] + displacement)):
            table[i, self.poleRanges[0][0]:self.poleRanges[0][1]] = 7
        
        for i in range(int(self.oneMan[1] + self.oneManStopperGap + displacement), int(self.oneMan[1] + self.oneManStopperGap + self.stopper + displacement)):
            table[i, self.poleRanges[0][0]:self.poleRanges[0][1]] = 2

    def addP2OneMan(self, table, displacement=0):

        for i in range(self.wall + displacement, self.wall + self.stopper + displacement):
            table[i, self.poleRanges[7][0]:self.poleRanges[7][1]] = 2
            
        for i in range(int(self.oneMan[0] + displacement), int(self.oneMan[1] + displacement)):
            table[i, self.poleRanges[7][0]:self.poleRanges[7][1]] = 7
        
        for i in range(int(self.oneMan[1] + self.oneManStopperGap + displacement), int(self.oneMan[1] + self.oneManStopperGap + self.stopper + displacement)):
            table[i, self.poleRanges[7][0]:self.poleRanges[7][1]] = 2   

    def addP1TwoMan(self, table, displacement=0):

        for i in range(self.wall + displacement, self.wall + self.stopper + displacement):
            table[i, self.poleRanges[1][0]:self.poleRanges[1][1]] = 2
            
        for i in range(int(self.twoMen[0][0] + displacement), int(self.twoMen[0][1] + displacement)):
            table[i, self.poleRanges[1][0]:self.poleRanges[1][1]] = 7

        for i in range(int(self.twoMen[1][0] + displacement), int(self.twoMen[1][1] + displacement)):
            table[i, self.poleRanges[1][0]:self.poleRanges[1][1]] = 7
        
        for i in range(int(self.twoMen[1][1] + displacement), int(self.twoMen[1][1]) + self.stopper + displacement):
            table[i, self.poleRanges[1][0]:self.poleRanges[1][1]] = 2

    def addP2TwoMan(self, table, displacement=0):

        for i in range(self.wall + displacement, self.wall + self.stopper + displacement):
            table[i, self.poleRanges[6][0]:self.poleRanges[6][1]] = 2
            
        for i in range(int(self.twoMen[0][0] + displacement), int(self.twoMen[0][1] + displacement)):
            table[i, self.poleRanges[6][0]:self.poleRanges[6][1]] = 7

        for i in range(int(self.twoMen[1][0] + displacement), int(self.twoMen[1][1] + displacement)):
            table[i, self.poleRanges[6][0]:self.poleRanges[6][1]] = 7
        
        for i in range(int(self.twoMen[1][1] + displacement), int(self.twoMen[1][1]) + self.stopper + displacement):
            table[i, self.poleRanges[6][0]:self.poleRanges[6][1]] = 2

    def addP1ThreeMan(self, table, displacement=0):
        for i in range(self.wall + displacement, self.wall + self.stopper + displacement):
            table[i, self.poleRanges[5][0]:self.poleRanges[5][1]] = 2
            
        for i in range(int(self.threeMen[0][0] + displacement), int(self.threeMen[0][1] + displacement)):
            table[i, self.poleRanges[5][0]:self.poleRanges[5][1]] = 7

        for i in range(int(self.threeMen[1][0] + displacement), int(self.threeMen[1][1] + displacement)):
            table[i, self.poleRanges[5][0]:self.poleRanges[5][1]] = 7

        for i in range(int(self.threeMen[2][0] + displacement), int(self.threeMen[2][1]) + displacement):
            table[i, self.poleRanges[5][0]:self.poleRanges[5][1]] = 7
        
        for i in range(int(self.threeMen[2][1] + displacement), int(self.threeMen[2][1]) + self.stopper + displacement):
            table[i, self.poleRanges[5][0]:self.poleRanges[5][1]] = 2

    def addP2ThreeMan(self, table, displacement=0):
        for i in range(self.wall + displacement, self.wall + self.stopper + displacement):
            table[i, self.poleRanges[2][0]:self.poleRanges[2][1]] = 2
            
        for i in range(int(self.threeMen[0][0] + displacement), int(self.threeMen[0][1] + displacement)):
            table[i, self.poleRanges[2][0]:self.poleRanges[2][1]] = 7

        for i in range(int(self.threeMen[1][0] + displacement), int(self.threeMen[1][1] + displacement)):
            table[i, self.poleRanges[2][0]:self.poleRanges[2][1]] = 7

        for i in range(int(self.threeMen[2][0] + displacement), int(self.threeMen[2][1]) + displacement):
            table[i, self.poleRanges[2][0]:self.poleRanges[2][1]] = 7
        
        for i in range(int(self.threeMen[2][1] + displacement), int(self.threeMen[2][1]) + self.stopper + displacement):
            table[i, self.poleRanges[2][0]:self.poleRanges[2][1]] = 2

    def addP1FiveMan(self, table, displacement=0):
        for i in range(self.wall + displacement, self.wall + self.stopper + displacement):
            table[i, self.poleRanges[3][0]:self.poleRanges[3][1]] = 2
            
        for i in range(int(self.fiveMen[0][0] + displacement), int(self.fiveMen[0][1] + displacement)):
            table[i, self.poleRanges[3][0]:self.poleRanges[3][1]] = 7

        for i in range(int(self.fiveMen[1][0] + displacement), int(self.fiveMen[1][1] + displacement)):
            table[i, self.poleRanges[3][0]:self.poleRanges[3][1]] = 7

        for i in range(int(self.fiveMen[2][0] + displacement), int(self.fiveMen[2][1] + displacement)):
            table[i, self.poleRanges[3][0]:self.poleRanges[3][1]] = 7

        for i in range(int(self.fiveMen[3][0] + displacement), int(self.fiveMen[3][1] + displacement)):
            table[i, self.poleRanges[3][0]:self.poleRanges[3][1]] = 7

        for i in range(int(self.fiveMen[4][0] + displacement), int(self.fiveMen[4][1] + displacement)):
            table[i, self.poleRanges[3][0]:self.poleRanges[3][1]] = 7

        for i in range(int(self.fiveMen[4][1] + displacement), int(self.fiveMen[4][1] + displacement) + self.stopper):
            table[i, self.poleRanges[3][0]:self.poleRanges[3][1]] = 2

    def addP2FiveMan(self, table, displacement=0):
        for i in range(self.wall + displacement, self.wall + self.stopper + displacement):
            table[i, self.poleRanges[4][0]:self.poleRanges[4][1]] = 2
            
        for i in range(int(self.fiveMen[0][0] + displacement), int(self.fiveMen[0][1] + displacement)):
            table[i, self.poleRanges[4][0]:self.poleRanges[4][1]] = 7

        for i in range(int(self.fiveMen[1][0] + displacement), int(self.fiveMen[1][1] + displacement)):
            table[i, self.poleRanges[4][0]:self.poleRanges[4][1]] = 7

        for i in range(int(self.fiveMen[2][0] + displacement), int(self.fiveMen[2][1] + displacement)):
            table[i, self.poleRanges[4][0]:self.poleRanges[4][1]] = 7

        for i in range(int(self.fiveMen[3][0] + displacement), int(self.fiveMen[3][1] + displacement)):
            table[i, self.poleRanges[4][0]:self.poleRanges[4][1]] = 7

        for i in range(int(self.fiveMen[4][0] + displacement), int(self.fiveMen[4][1] + displacement)):
            table[i, self.poleRanges[4][0]:self.poleRanges[4][1]] = 7

        for i in range(int(self.fiveMen[4][1] + displacement), int(self.fiveMen[4][1] + displacement) + self.stopper):
            table[i, self.poleRanges[4][0]:self.poleRanges[4][1]] = 2

    def buildTable(self, displacements, ball_position):

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
            
        poleRanges = self.poleRanges
        

        
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



        self.addP1OneMan(table, displacements['P1OneMan'])
        self.addP2OneMan(table, displacements['P2OneMan'])
        self.addP1TwoMan(table, displacements['P1TwoMan'])
        self.addP2TwoMan(table, displacements['P1TwoMan'])
        self.addP1ThreeMan(table, displacements['P1ThreeMan'])
        self.addP2ThreeMan(table, displacements['P1ThreeMan'])
        self.addP1FiveMan(table, displacements['P1FiveMan'])
        self.addP2FiveMan(table, displacements['P1FiveMan'])

        #add Ball

        ballPositionY, ballPositionX = ball_position
        

        ballY = (int(ballPositionY - self.ballDiameter / 2), int(ballPositionY + self.ballDiameter / 2))
        ballX = (int(ballPositionX - self.ballDiameter / 2), int(ballPositionX + self.ballDiameter / 2))

        for i in range(ballX[0], ballX[1]):

            table[i, ballY[0]:ballY[1]] = 8

        return table
 

    def find_valid_angles(self, ballPosition, matrix):
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
                # Plot the line using only the endpoints
                valid_angles.append((x, y))

        print(valid_angles)
        return valid_angles
    

    def calculate_range_of_angles(self, valid_angles):

        if len(valid_angles) == 0:
            return "No Valid Shots"

        range_of_angles = []

        a1, b1 = np.abs(valid_angles[0][0][0] - valid_angles[0][0][1]) , (valid_angles[0][1][0] - valid_angles[0][1][1])
        print(b1, a1)

        # Calculate the tangent of the angle
        tangent1 = b1 / a1
        
        # Find the angle in radians using the inverse tangent function
        angle_rad1 = math.atan(tangent1)
        
        # Convert the angle from radians to degrees
        angle_deg1 = np.round(math.degrees(angle_rad1),2)

        range_of_angles.append(angle_deg1)


        #### last in list of valid lines

        a2, b2 = np.abs(valid_angles[-1][0][0] - valid_angles[-1][0][1]) , (valid_angles[-1][1][0] - valid_angles[-1][1][1])
        print(b2, a2)

        # Calculate the tangent of the angle
        tangent2 = b2 / a2
        
        # Find the angle in radians using the inverse tangent function
        angle_rad2 = math.atan(tangent2)
        
        # Convert the angle from radians to degrees
        angle_deg2 = np.round(math.degrees(angle_rad2), 2)

        range_of_angles.append(angle_deg2)       


        return range_of_angles



displacement_sliders = {
    "P1OneMan": 0,
    "P2OneMan": 0,
    "P1TwoMan": 0,
    "P2TwoMan": 0,
    "P1ThreeMan": 0,
    "P2ThreeMan": 0,
    "P1FiveMan": 0,
    "P2FiveMan": 0
}



# Instantiate the Table class
table = Table()

# Initial ball position
ball_x_initial = 555
ball_y_initial = table.width / 2



ballPosition = {
    "ball_x": int(ball_x_initial),
    "ball_y": int(ball_y_initial),
}

# Build the foosball table matrix
matrix = table.buildTable(displacement_sliders, (ballPosition['ball_x'], ballPosition['ball_y']))

fig, ax = plt.subplots(figsize=(10, 8))
plt.subplots_adjust(bottom=0.4, left=0.1, right=0.9, top=0.95)
plt.imshow(matrix, cmap='viridis')


# Plot the initial ball position
ball_plot, = plt.plot(ballPosition['ball_x'], ballPosition['ball_y'], 'ro')

# Slider for adjusting ball position
ax_ball_position = plt.axes([0.2, 0.25, 0.65, 0.03])
slider_ball_position_x = Slider(ax_ball_position, 'Ball Position X', 40, table.length - 40, valinit=ball_x_initial)

# Slider for adjusting ball position
ay_ball_position = plt.axes([0.05, 0.5, 0.03, 0.4])
slider_ball_position_y = Slider(ay_ball_position, 'Ball Position Y', 40, table.width - 40, valinit=ball_y_initial, orientation='vertical')
# Invert the slider range and adjust the limits
slider_ball_position_y.set_val(table.width - slider_ball_position_y.val)

# Slider for adjusting displacement of P1 OneMan
ax_p1_oneman_displacement = plt.axes([0.15, 0.2, 0.3, 0.03])
slider_p1_oneman_displacement = Slider(ax_p1_oneman_displacement, 'P1 OneMan', 0, 160, valinit=0)

# Slider for adjusting displacement of P2 OneMan
ax_p2_oneman_displacement = plt.axes([0.6, 0.2, 0.3, 0.03])
slider_p2_oneman_displacement = Slider(ax_p2_oneman_displacement, 'P2 OneMan', 0, 160, valinit=0)

# Slider for adjusting displacement of P1 twoman
ax_p1_twoman_displacement = plt.axes([0.15, 0.15, 0.3, 0.03])
slider_p1_twoman_displacement = Slider(ax_p1_twoman_displacement, 'P1 TwoMan', 0, 160, valinit=0)

# Slider for adjusting displacement of P2 twoman
ax_p2_twoman_displacement = plt.axes([0.6, 0.15, 0.3, 0.03])
slider_p2_twoman_displacement = Slider(ax_p2_twoman_displacement, 'P2 TwoMan', 0, 160, valinit=0)

# Slider for adjusting displacement of P1 threeman
ax_p1_threeman_displacement = plt.axes([0.15, 0.1, 0.3, 0.03])
slider_p1_threeman_displacement = Slider(ax_p1_threeman_displacement, 'P1 ThreeMan', 0, 160, valinit=0)

# Slider for adjusting displacement of P2 threeman
ax_p2_threeman_displacement = plt.axes([0.6, 0.1, 0.3, 0.03])
slider_p2_threeman_displacement = Slider(ax_p2_threeman_displacement, 'P2 ThreeMan', 0, 160, valinit=0)

# Slider for adjusting displacement of P1 fiveman
ax_p1_fiveman_displacement = plt.axes([0.15, 0.05, 0.3, 0.03])
slider_p1_fiveman_displacement = Slider(ax_p1_fiveman_displacement, 'P1 FiveMan', 0, 160, valinit=0)

# Slider for adjusting displacement of P2 fiveman
ax_p2_fiveman_displacement = plt.axes([0.6, 0.05, 0.3, 0.03])
slider_p2_fiveman_displacement = Slider(ax_p2_fiveman_displacement, 'P2 FiveMan', 0, 160, valinit=0)


def update_p1_oneman_displacement(val):
    displacement_sliders["P1OneMan"] = int(val)
    new_matrix = table.buildTable(displacement_sliders, (ballPosition['ball_x'], ballPosition['ball_y']))
    ax.imshow(new_matrix, cmap='viridis')
    fig.canvas.draw_idle()

def update_p2_oneman_displacement(val):
    displacement_sliders["P2OneMan"] = int(val)
    new_matrix = table.buildTable(displacement_sliders, (ballPosition['ball_x'], ballPosition['ball_y']))
    ax.imshow(new_matrix, cmap='viridis')
    fig.canvas.draw_idle()

def update_p1_twoman_displacement(val):
    displacement_sliders["P1TwoMan"] = int(val)
    new_matrix = table.buildTable(displacement_sliders, (ballPosition['ball_x'], ballPosition['ball_y']))
    ax.imshow(new_matrix, cmap='viridis')
    fig.canvas.draw_idle()

def update_p2_twoman_displacement(val):
    displacement_sliders["P2TwoMan"] = int(val)
    new_matrix = table.buildTable(displacement_sliders, (ballPosition['ball_x'], ballPosition['ball_y']))
    ax.imshow(new_matrix, cmap='viridis')
    fig.canvas.draw_idle()

def update_p1_threeman_displacement(val):
    displacement_sliders["P1ThreeMan"] = int(val)
    new_matrix = table.buildTable(displacement_sliders, (ballPosition['ball_x'], ballPosition['ball_y']))
    ax.imshow(new_matrix, cmap='viridis')
    fig.canvas.draw_idle()

def update_p2_threeman_displacement(val):
    displacement_sliders["P2ThreeMan"] = int(val)
    new_matrix = table.buildTable(displacement_sliders, (ballPosition['ball_x'], ballPosition['ball_y']))
    ax.imshow(new_matrix, cmap='viridis')
    fig.canvas.draw_idle()

def update_p1_fiveman_displacement(val):
    displacement_sliders["P1FiveMan"] = int(val)
    new_matrix = table.buildTable(displacement_sliders, (ballPosition['ball_x'], ballPosition['ball_y']))
    ax.imshow(new_matrix, cmap='viridis')
    fig.canvas.draw_idle()

def update_p2_fiveman_displacement(val):
    displacement_sliders["P2FiveMan"] = int(val)
    new_matrix = table.buildTable(displacement_sliders, (ballPosition['ball_x'], ballPosition['ball_y']))
    ax.imshow(new_matrix, cmap='viridis')
    fig.canvas.draw_idle()   

angle_text_annotations = []

def find_angles_from_position(event):
    global angle_text_annotations

    displacement_sliders["P1OneMan"] = int(slider_p1_oneman_displacement.val)
    displacement_sliders["P2OneMan"] = int(slider_p2_oneman_displacement.val)
    displacement_sliders["P1TwoMan"] = int(slider_p1_twoman_displacement.val)
    displacement_sliders["P2TwoMan"] = int(slider_p2_twoman_displacement.val)
    displacement_sliders["P1ThreeMan"] = int(slider_p1_threeman_displacement.val)
    displacement_sliders["P2ThreeMan"] = int(slider_p2_threeman_displacement.val)
    displacement_sliders["P1FiveMan"] = int(slider_p1_fiveman_displacement.val)
    displacement_sliders["P2FiveMan"] = int(slider_p2_fiveman_displacement.val)
    
    ball_y = ballPosition['ball_y']
    ball_x = ballPosition['ball_x']

    new_matrix = table.buildTable(displacement_sliders, (ball_x, ball_y))
    ax.imshow(new_matrix, cmap='viridis')
    fig.canvas.draw_idle()
    
    valid_angles = table.find_valid_angles((ball_x, ball_y), new_matrix)

    range_of_angles = table.calculate_range_of_angles(valid_angles)

    for line in ax.lines:
        line.remove()

    for line in valid_angles:
        x, y = line
        ax.plot([x[0], x[1]], [y[0], y[1]], color="white")

    ball_plot.set_data(ball_x, ball_y)
    fig.canvas.draw_idle()

    # Remove previously plotted text annotations
    for text_annotation in angle_text_annotations:
        text_annotation.remove()
    angle_text_annotations = []

    # Convert range_of_angles to a readable string
    if type(range_of_angles) == str:
        angle_text = range_of_angles
    else:
        angle_text = f"[{range_of_angles[0]}" + chr(176) + ' , ' + f"{range_of_angles[1]}" + chr(176) + "]"

    # Add the text annotation to the plot
    text_annotation = ax.text(ball_x - 100, ball_y- 20, angle_text, fontsize=12, ha='center', va='bottom', color='white')
    angle_text_annotations.append(text_annotation)

    update_x(slider_ball_position_x.val)
    update_y(slider_ball_position_y.val)
    print(range_of_angles)


slider_p1_oneman_displacement.on_changed(update_p1_oneman_displacement)
slider_p2_oneman_displacement.on_changed(update_p2_oneman_displacement)
slider_p1_twoman_displacement.on_changed(update_p1_twoman_displacement)
slider_p2_twoman_displacement.on_changed(update_p2_twoman_displacement)
slider_p1_threeman_displacement.on_changed(update_p1_threeman_displacement)
slider_p2_threeman_displacement.on_changed(update_p2_threeman_displacement)
slider_p1_fiveman_displacement.on_changed(update_p1_fiveman_displacement)
slider_p2_fiveman_displacement.on_changed(update_p2_fiveman_displacement)


ax_button_confirm_pieces = plt.axes([0.4, 0.3, 0.2, 0.04])
button_confirm_pieces = Button(ax_button_confirm_pieces, 'Find Angles')
button_confirm_pieces.on_clicked(find_angles_from_position)

def update_x(val):
    ballPosition['ball_y'] = ballPosition['ball_y']
    ballPosition['ball_x'] = int(val)
    new_matrix = table.buildTable(displacement_sliders, (ballPosition['ball_x'], ballPosition['ball_y']))
    ax.imshow(new_matrix, cmap='viridis')
    fig.canvas.draw_idle()

def update_y(val):
    ballPosition['ball_y'] = int(val)
    ballPosition['ball_x'] = ballPosition['ball_x']
    new_matrix = table.buildTable(displacement_sliders, (ballPosition['ball_x'], ballPosition['ball_y']))
    ax.imshow(new_matrix, cmap='viridis')
    fig.canvas.draw_idle()


slider_ball_position_x.on_changed(update_x)
slider_ball_position_y.on_changed(update_y)


plt.show()
