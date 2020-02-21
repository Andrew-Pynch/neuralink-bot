# neuralink-bot
Neuralink posses a robot capable of lacing a brain with "threads" containing electrodes. I am not sure if they posses the capability to automatically localize and avoid blood vessels while placing these threads. It appears that the surgery processes requries neurosurgeon supervision to select lacing sites that "dodge" blood vessels.

[Clip From Neuralink Presentation](neuralink.gif)

## Roadmap
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

