try:
    import sys
    sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
except:
    print('okay')

import cv2
import math
import numpy as np

from helper_functions import *

class Thread: # Note, often times in my writing I use thread and lace iterchangably to describe neural lace
    def __init__(self, SIZE):
        self.SIZE = SIZE
        self.x = np.random.randint(0, SIZE)
        self.y = np.random.randint(0, SIZE)

    def __str__(self):
        return f"x:{self.x}, y:{self.y}"

    def action(self, choice):
        """Choose between 5 actions
        Up, Down, Left, Right, or Place Electrode Thread
        """
        if choice == 0:
            self.move(x=1, y=1)
        elif choice == 1:
            self.move(x=-1, y=-1)
        elif choice == 2:
            self.move(x=-1, y=1)
        elif choice == 3:
            self.move(x=1, y=-1)
        
    def move(self, x=False, y=False):
        # If no value for x, move randomly
        if not x:
            self.x += np.random.randint(-1, 2)
        else:
            self.x += x

        # If no value for y, move randomly
        if not y:
            self.y += np.random.randint(-1, 2)
        else:
            self.y += y

        # If we are out of bounds, fix!
        if self.x < 0:
            self.x = 0
        elif self.x > self.SIZE-1:
            self.x = self.SIZE-1
        if self.y < 0:
            self.y = 0
        elif self.y > self.SIZE-1:
            self.y = self.SIZE-1

    def distance(self, vessel_image, distance_dict):
        """Compute distance between a electrode thread and the nearest blood vessel
        
        Arguments:
            vessel_image {[nparray]} -- [input image of segmented vasculature]
        """
        # Compute all possible distances between self and other pixels
        for i in range(len(vessel_image)):
            for j in range(len(vessel_image)):
                if black_pixel_bool(vessel_image, i, j) == True:
                    result = euc_dist([i, j], [self.y, self.x])

                    distance_dict.add((i, j), result)
        
        running_min = min(distance_dict.values())
        smallest_distance = [key for key in distance_dict if distance_dict[key] == running_min]

        x = smallest_distance[0][0]
        y = smallest_distance[0][1]
           
        # Return the coordinates of the nearest vessel
        return distance_dict.get((x, y))

class Distances(dict):
    """Distance Dictionary Object"""
    def __init__(self):
        self = dict()
    
    def add(self, key, value):
        self[key] = value
