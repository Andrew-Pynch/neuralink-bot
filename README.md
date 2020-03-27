# neuralink-bot
I am going to train a learner to select iamge reigons that maximize the distance from blood vessel areas. The process is meant to emulate the requirements that a robot performing neurosurgery might have to conform to when inserting electrodes into the brain

This project started because Neuralink posses a robot capable of lacing a brain with "threads" containing electrodes. I am not sure however if they posses the capability to automatically localize and avoid blood vessels while placing these threads. It appears that the surgery processes requries neurosurgeon supervision to select lacing sites that "dodge" blood vessels.

![Alt Text](https://media0.giphy.com/media/Jr5RD7ns1m2dRKa8go/200.webp)


# Cool Things I'm Working On Right Now
# Part 1
## Learning Thread Placement W/ Q Learning
Before I got fancy with any DQN or my new research interest HER(Heindsight Experience Replay), I decided to start with the most basic reinforcement learning algorithm.
By performing color segementation of the video clip from the Neuralink presentation I produced a binary color mask which "sort of" reveals blood vessels. This is just a bodged together sollution until I can train a model to perform semantic segmentation of blood vessels (part 2)

![Alt Text](https://media.giphy.com/media/WRtuHhi0aqjzNImQxE/giphy.gif)

After creating these binary masks, I further cropped them down to small squares so that I could run my Q Learning experiments efficiently. Here is a gif of the "learners" early exploration of
the environment with the goal of maximizing its distance from blood vessels. 

![Alt Text](https://media0.giphy.com/media/lqwO9rFre3Guf2pvLh/giphy.webp)

Here is the reward the Q Table yielded over time 25,000 epochs.

![Alt Text](https://github.com/Andrew-Pynch/neuralink-bot/blob/master/RL/Custom_Env/25000_epochs.png?raw=true)

This was a great hands on learning experience with Q Learning which helped me cautify 
the knowledge that had once been entirely theoretical

# Part 2
## Notice Of Temporary Development Freeze
Part 2 of this project involves training a model to segment blood vessels out of an image. My early experiments with 100 manually labelled images extracted from the Neuralink presentation did not yield sufficent results. 

I believe that in order to train a sufficiently capable model, two things will have to hapen. 
1. Neuralink (or another research insitution) will need to supply with additional images of tissue containing blood vessels similar to the scale captured by the Neuralink robot during surgery
2. Labelling images
a. Buckle down and manually segmented thousands of images to extract the blood vessels from an image
b. Pay someone else to perform this laborious labelling. Amazon Mechanical Turk?

Either way, I feel the scope and scale of this stage of the project is beyond the resources (time and monetary) that I have available to me.

## Sematic Segmentation of Blood Vessels & Max Distance Prediction
Right now I am working on creating a model that can automatically segment blood vessels given an input image. Some work has been done in this area using a small dataset of eye vasculature within the [DRIVE](https://drive.grand-challenge.org/) dataset.

Currently, this involves lots of manuall labelling to produce images like this.
![Alt Text](https://i.imgur.com/4jfcB6A.jpg)

Once the model is satisfactorially performant, I am going to compute 10 points within the image that are maximally distant from the pixles containing blood vessels. These point labels will then train a regression head to predict the coordinates of points within an input image that are maximally far away from blood vessels.

This will be similar to this model which was trained to predict where the center of a persons face was except in our case its predicting which areas maximize distance from vasculature. 

![Alt Text](https://i.imgur.com/jTeTGB1.png)

# Part 3
## Advanced Reinforcement Learning approaches
This whole project merely serves as a way for me to advance my Deep Learning skills while exploring something I am passionate about. To be honest, I have no idea which formulation of my problem statement will lead to the best system for selecting thread insertion sites.

In this section I can going to explore advanced methods in Reinforcement Learning to see if RL formulations of the problem lead to better results the Q - Learning or Semantic Segmentation with coordinate regression. 
