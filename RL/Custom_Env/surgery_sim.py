import sys
#sys.path.remove('/opt/ros/kinetic/lib.python2.7/dist-packages')

import neural_thread
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
COLLISION_PENALTY = 300
AVOID_COLLISION_REWARD = 25

epsilon = 0.998
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
    q_table = np.random.rand(SIZE, SIZE)
else:
    with open(start_q_table, "rb") as f:
        q_table = pickle.load(f)

################
# MAIN SIM BLOCK
################
episode_rewards = []

for episode in range(NUM_EPISODES):
    ########
    # Render
    ########
    if episode % SHOW_EVERY == 0:
        print(f"on #{episode}, epsilon is {epsilon}")
        print(f"{SHOW_EVERY} ep mean: {np.mean(episode_rewards[-SHOW_EVERY:])}")
        show = True 
    else:
        show = False

    #####################
    # Reward Calculations
    #####################
    episode_reward = 0
    for i in range(200):
        COLLISION = False
        main_thread = neural_thread.Thread(SIZE)
        distance_obj = neural_thread.Distances()

        observation = int(main_thread.distance(VESSEL_IMG, distance_obj))

        ##############
        # EXPLOITATION
        ##############
        if np.random.random() > epsilon:
            # Get the optimal action from the Q Table
            action = np.argmax(q_table[observation])
        else:
            action = np.random.randint(0, 4)
        # Take the action selected
        main_thread.action(action)

        ###################################
        # CALCULATING REWARD
        ###################################
        if black_pixel_bool(VESSEL_IMG, main_thread.x, main_thread.y) == True:
            reward = -COLLISION_PENALTY
            COLLISION = True
        else:
            reward = -main_thread.distance(VESSEL_IMG, distance_obj)
        
        ##################
        # NEXT OBSERVATION
        ##################
        new_observsation = int(main_thread.distance(VESSEL_IMG, distance_obj))
        max_future_q = np.max(q_table[new_observsation])
        current_q = q_table[observation][action]

        if COLLISION == False:
            new_q = AVOID_COLLISION_REWARD
        else:
            new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)
        q_table[observation][action] = reward



        
        episode_reward += reward
        if COLLISION == True or COLLISION == False:
            break


    ############################
    # VISUALIZATION ON SHOWEVERY
    ############################
    implot = plt.imshow(VESSEL_IMG)
    plt.scatter(x=main_thread.x, y=main_thread.y, c='g', s=40)
    plt.savefig(f'renders/{episode}.jpg')
    plt.clf()

    

    #################
    # EPISODE METRICS
    #################
    print(f'EPISODE: {episode}| REWARD: {episode_reward}')
    print(f'X: {main_thread.x} Y: {main_thread.y}')

    episode_rewards.append(episode_reward)
    epsilon *= EPS_DECAY

moving_avg = np.convolve(episode_rewards, np.ones((SHOW_EVERY,))/SHOW_EVERY, mode='valid')

plt.plot([i for i in range(len(moving_avg))], moving_avg)
plt.ylabel(f"Reward {SHOW_EVERY}ma")
plt.xlabel("episode #")
plt.show()

with open(f"qtable-{int(time.time())}.pickle", "wb") as f:
    pickle.dump(q_table, f)
            
        

    

