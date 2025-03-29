from math import cos, sin, sqrt
from random import randint
import random
from typing import List


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.center = [x_center, y_center]

    def randPoint(self) -> List[float]:
        theta = randint(0, 360)
        rand_radius = self.radius * sqrt(random.random())
        # Parametric equations of a circle not centered at origin (h,k)
        # x = h + rcos(theta), y = k + rcos(theta)
        # xCoord = self.center[0] + (self.radius * cos(theta))
        # yCoord = self.center[1] + (self.radius * sin(theta))
        
        xCoord = self.center[0] + (rand_radius * cos(theta))
        yCoord = self.center[1] + (rand_radius * sin(theta))
        return [xCoord, yCoord]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()