# neuralink-bot
Neuralink posses a robot capable of lacing a brain with "threads" containing electrodes. I am not sure if they posses the capability to automatically localize and avoid blood vessels while placing these threads. It appears that the surgery processes requries neurosurgeon supervision to select lacing sites that "dodge" blood vessels.

I am going to create a simple pygame that simulates blood vessels and the placement of threads. After the basic game is complete I will see if I can develop some approaches for avoiding blood vessels during thread placement

# Rules
- 60 Second Time Limit
- 10 Threads To "Sew"
- Maximize distance from blood vessels
- Lose points if you collide with a "Blood Vessel"

# Play instructions
Movement of the surgial robot (pictured currently with a blue dot) can be achieved with the arrow keys

To place a lace within the brain, press backspace. NOTE: This is kinda broken in that you have to press it twice (its rendering behind???)

# Using this repo
To run any of the example games or the main surgery simulation run
```pip install -r requirements.txt```

