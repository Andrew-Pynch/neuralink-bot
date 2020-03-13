# TEMPORARY DEVELOPMENT FREEZE
I am currently inundated with my full time job and school. I will return to this project 3/21/2020

# neuralink-bot
Neuralink posses a robot capable of lacing a brain with "threads" containing electrodes. I am not sure if they posses the capability to automatically localize and avoid blood vessels while placing these threads. It appears that the surgery processes requries neurosurgeon supervision to select lacing sites that "dodge" blood vessels.

![](https://media.giphy.com/media/Jr5RD7ns1m2dRKa8go/giphy.gif)

## Roadmap
NOTE: I have been reading lots of books and taking a MOOC on robotics and am coming to the conclusion that I need to reconsider the way I am trying to construct the simulation. Within the ethos of work smarter not harder, developing this simulation from scratch is seeming to be more of an impediment than it needs to be. 

Once I finish up this term of school and am blessed with more freetime I think I am going to wipe the slate clean and start from scratch with some of the tools I have been learning over the last couple weeks

-1a. Develop simple 2 simulation loosely based off of Neuralinks Brain Surgery Process: X - WE ARE HERE
-1b. Train reinforcement learning algorithm to choose good "lace" selection sites
Note: Nieve score function should encourage maximal distance from "vessels" and other lace that has already been placed.

-2a. Refactor simluation to be a fully rendered 3d env
-2b. Retrain model in 3d simulation

-3a. Request video footage of brain surgery from neuralink
-3b. Segment blood vessels within video footage
-3c. Retrain model on actual video footage provided by neuralink.

# Rules
- 60 Second Time Limit
- 10 Threads To "Sew"
- Maximize distance from blood vessels
- Lose points if you collide with a "Blood Vessel"

# Play instructions
- Movement = Arrow Keys
- Place Neural Lace = BackSpace

# Using this repo
To run any of the example games or the main surgery simulation run
```pip install -r requirements.txt```

