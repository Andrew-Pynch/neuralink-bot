import sys
#sys.path.remove('/opt/ros/kinetic/lib.python2.7/dist-packages')

import neur
from helper_functions import *

import time 
import pickle 
import cv2 
import numpy as np
from PIL import Image 
import matplotlib.pyplot as plt 
from matplotlib import style

style.use('ggplot')

######################
# SIMULATION CONSTANTS
######################

SIZE = 150 # Size of the thread

NUM_EPISODES = 25000
MOVE_PENALTY = 1
RUPTURE_PENALY = 300

epsilon = 0
EPS_DECAY = 0.9998 # Every episode will be epsilon * EPS_DECAY
SHOW_EVERY = 500 # Render the simulation every 500 iterations

start_q_table = None 

LEARNING_RATE = 0.1
DISCOUNT = 0.95 

left_squares = order_files_by_date(
    "/home/andrew/Github/neuralink-bot/Image_Segmentation/segmented_images/square_segmentation_crops/left_crop/", 
    ".jpg")
VESSEL_IMG = get_example_image(left_squares, 0)

THREAD_K = 1 # Thread key in color dict
VES_K = 2 # Vessel key in color dict
TISSUE_K = 3 # Tieeu key in color dict

d = {1: (255, 175, 0),
     2: (255, 255, 255), # Black Vessels
     3: (0, 0, 0)} # White neural tissue


###################
# Previous Q-Table? 
###################
if start_q_table is None:
    # initialize the q-table#
    q_table = {}
    for i in range(-SIZE+1, SIZE):
        for ii in range(-SIZE+1, SIZE):
            for iii in range(-SIZE+1, SIZE):
                    for iiii in range(-SIZE+1, SIZE):
                        q_table[((i, ii), (iii, iiii))] = [np.random.uniform(-5, 0) for i in range(4)]
else:
    with open(start_q_table, "rb") as f:
        q_table = pickle.load(f)

################
# MAIN SIM BLOCK
################
episode_rewards = []

for episode in range(NUM_EPISODES):
    main_thread = thread.Thread(SIZE)
    print(main_thread.__str__())

