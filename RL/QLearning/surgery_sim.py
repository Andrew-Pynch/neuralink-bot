import sys
sys.path.remove('/opt/ros/kinetic/lib.python2.7/dist-packages')

import time 
import pickle 
import cv2 
import numpy as np
from PIL import image 
import matplotlib.pyplot as plt 
from matplotlib import style

style.use('ggplot')

######################
# SIMULATION CONSTANTS
######################

SIZE = 60 # Size of the thread

NUM_EPISODES = 25000
MOVE_PENALTY = 1
RUPTURE_PENALY = 300

epsilon = 0
EPS_DECAY = 0.9998 # Every episode will be epsilon * EPS_DECAY
SHOW_EVERY = 500 # Render the simulation every 500 iterations

start_q_table = None 

LEARNING_RATE = 0.1
DISCOUNT = 0.95 

ROBOT_N = 1
VESSELS = "/home/andrew/Github/neuralink-bot/Image_Segmentation/segmented_images/left_crop/_left_crop0.jpg"

d = {1: (255, 175, 0),
     2: (255, 255, 255), # Black Vessels
     3: (0, 0, 0)} # White neural tissue
    
class Thread: # Note, often times in my writing I use thread and lace iterchangably to describe neural lace
    def __init__(self):
        self.x = np.random.randint(0, SIZE)
        self.y = np.random.randint(0, SIZE)

    def __str__(self):
        return f"{self.x}, {self.y}"
    
    def __sub__(self, vessel_image):
        