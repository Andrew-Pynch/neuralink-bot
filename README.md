# neuralink-bot
I am going to train a learner to select iamge reigons that maximize the distance from blood vessel areas. The process is meant to emulate the requirements that a robot performing neurosurgery might have to conform to when inserting electrodes into the brain

This project started because Neuralink posses a robot capable of lacing a brain with "threads" containing electrodes. I am not sure however if they posses the capability to automatically localize and avoid blood vessels while placing these threads. It appears that the surgery processes requries neurosurgeon supervision to select lacing sites that "dodge" blood vessels.

![](https://media.giphy.com/media/Jr5RD7ns1m2dRKa8go/giphy.gif)


# Cool Things I'm Working On Right Now


![](/Image_Segmentation/image_manipulation/segmented_images/recombined_gifs/top_segs.gif)


(Everything referenced)
Before I can begin the exciting reinforcement learning, I need to setup a 
playground where my bot can learn. Initially I was going to simulate blood vessels by drawing overlapping fractal trees that "kind of" simulated blood vessels. This fractal vessel simulation was done in pygame and had a couple of huge drawbacks. It was buggy, slow, and unrealistic.

Considering all the downside I decided to scrap all that work and start from scratch.

1. Video capture the microscope view pictured above from the Neuralink summer presentation
2. Split the video into a folder of jpgs (1 for each frame of the video)
3. Crop the top half, top left, and top right section of each image in the folder of extracted jpg files
4. Apply a nieve binary color mask to "reveal" blood vessels. 
5. Save eached masked image into the appropriate directory (top, left, and right)
6. Recombine folders of cropped and masked jpgs into gifs 


![](/Image_Segmentation/segmented_images/recombined_gifs/left_segs.gif)


# Roadmap
## 1.) Develop Simulation Environment
At the core of Reinforcement learning is the notion of feedback. Before a learned can learn, it needs an environment to do so. While the details are still fuzzy, I essentially need to create a simulation of the close of microscope brain view pictured above.

The basic requirements are
1. Simulate Vascular Structure
2. Simulate motion of vasculature due to heartbeat / breathing
3. Simulate placing of neural lace within this dynamic environment.
4. Score function: Higher score when distance from moving vessels is maxed? (this is subject to change) 

## 2.) Reinforcement Learning
This is where I will be challeneged to grow the most. While I understand the theoretical elements of reinforcement learning, my practical knowledge is lacking. If I am to take Feynmans "What I cannot create I do not understand" maxim to heart, I really don't understand RL. This will be my first time performing RL in a novel environment. 

## 3.) ?
What comes after this is unknown. I have no idea how well the learner will perform or what ides for continued improvement might reveal themselves

# Tree Segmentation --> Blood Vessel Segmentation?
If I were to take the top layers off of a seg net that had previously been trained to perform semantic segmentation on trees, I might be able to use that encoded knowledge to learn to segment blood vessels using a few hundred labelled images?? I am not sure on this one... I am only going to experiment with this after I have finished the simulation and trained the learner in the simulated environment. 
