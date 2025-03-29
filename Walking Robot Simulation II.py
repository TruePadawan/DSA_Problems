from typing import List

'''
Basic Approach - Was not sufficient (TLE for large test-cases)

For each step to be taken:
    Check if robot is at the edge based on its current direction
    
    Conditions based on current direction:
    North -> Check that yPos == height - 1
    South -> Check that yPos == 0
    East -> Check that xPos == width - 1
    West -> Check that xPos == 0
    
    If at edge:
        Set direction to the counterclockwise direction
    Else:
        move one step:
            If East/West, increment/decrement the xPos
            If North/South, increment/decrement the yPos
'''

class InefficientRobot:

    def __init__(self, width: int, height: int):
        self.bounds = [width-1, height-1]
        self.position = [0,0]
        self.current_direction = "East"
        self.next_direction = {
            "East": "North",
            "North": "West",
            "West": "South",
            "South": "East"
        }

    def step(self, num: int) -> None:
        while num > 0:
            # Prevent collision by checking if it's at the edge
            at_edge = False
            match self.current_direction:
                case "North":
                    at_edge = self.position[1] == self.bounds[1]
                case "South":
                    at_edge = self.position[1] == 0
                case "East":
                    at_edge = self.position[0] == self.bounds[0]
                case "West":
                    at_edge = self.position[0] == 0
            
            if at_edge:
                self.current_direction = self.next_direction[self.current_direction]
            else:
                match self.current_direction:
                    case "North":
                        self.position[1] += 1
                    case "South":
                        self.position[1] -= 1
                    case "East":
                        self.position[0] += 1
                    case "West":
                        self.position[0] -= 1
                num -= 1
        

    def getPos(self) -> List[int]:
        return self.position

    def getDir(self) -> str:
        return self.current_direction


'''
More efficient method

While number of steps > 0:
    Will the robot go out of bounds in its current dir if it takes 'num' amount of steps?
    Is num > (edgePos - currentPos)
    If yes, move to the edge:
        How many steps is required to get to the edge? (edgePos - currentPos)
        Subtract it from num
        increment/decrement relevent pos by (edgePos - currentPos)
        Go to next direction
    Else:
        increment/decrement relevent pos by num
        n = 0
            
'''

class Robot:

    def __init__(self, width: int, height: int):
        self.bounds = [width-1, height-1]
        self.position = [0,0]
        self.current_direction = "East"
        self.next_direction = {
            "East": "North",
            "North": "West",
            "West": "South",
            "South": "East"
        }

    def step(self, num: int) -> None:
        while num > 0:
            steps_needded_to_get_to_edge = 0
            match self.current_direction:
                    case "North":
                        steps_needded_to_get_to_edge = self.bounds[1] - self.position[1]
                    case "South":
                        steps_needded_to_get_to_edge = self.position[1]
                    case "East":
                        steps_needded_to_get_to_edge = self.bounds[0] - self.position[0]
                    case "West":
                        steps_needded_to_get_to_edge = self.position[0]
            
            if num > steps_needded_to_get_to_edge:
                # Move to the edge of the current direction
                match self.current_direction:
                    case "North":
                        self.position[1] += steps_needded_to_get_to_edge
                    case "South":
                        self.position[1] -= steps_needded_to_get_to_edge
                    case "East":
                        self.position[0] += steps_needded_to_get_to_edge
                    case "West":
                        self.position[0] -= steps_needded_to_get_to_edge
                num -= steps_needded_to_get_to_edge
                self.current_direction = self.next_direction[self.current_direction]
            else:
                match self.current_direction:
                    case "North":
                        self.position[1] += num
                    case "South":
                        self.position[1] -= num
                    case "East":
                        self.position[0] += num
                    case "West":
                        self.position[0] -= num
                num = 0
                

    def getPos(self) -> List[int]:
        return self.position

    def getDir(self) -> str:
        return self.current_direction

robot = Robot(6, 3) # Initialize the grid and the robot at (0, 0) facing East.
robot.step(2)  # It moves two steps East to (2, 0), and faces East.
robot.step(2)  # It moves two steps East to (4, 0), and faces East.
robot.getPos() # return [4, 0]
robot.getDir() # return "East"
robot.step(2)  # It moves one step East to (5, 0), and faces East.
                # Moving the next step East would be out of bounds, so it turns and faces North.
                # Then, it moves one step North to (5, 1), and faces North.
robot.step(1)  # It moves one step North to (5, 2), and faces North (not West).
robot.step(4)  # Moving the next step North would be out of bounds, so it turns and faces West.
                # Then, it moves four steps West to (1, 2), and faces West.
robot.getPos() # return [1, 2]
robot.getDir() # return "West"