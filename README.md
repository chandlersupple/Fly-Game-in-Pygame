Fly-Game-in-Pygame

CONTROLS
Control 'sprites' with the arrow keys, and change your 'sprite' with the 'a', 's', 'd', and 'w' keys. 

CODE EXPLANATION
Environment includes:
Clouds - Using a simple 'if' statement, the clouds loop as a variable 'x' is increased to a certain threshold, then set to 0 when said threshold has been met
Bird - The bird's semi-organic motion is the result of a modified sine wave with the function 'y = 100*(sin(0.5*(x)))'. The image itself origionates from the Internet, and is imported when the code is ran.
Sprite - Sprites origionate from the Internet, and are controlled via a constant input system which is updating at a rate of 60 frames per seconds (fps). 

**NOTE
If running on an older computer, ensure your monitor has a refresh rate of 60 frames per second, as otherwise, the game may appear 'choppy'. Most standard computers are equipped with such equipped with such systems.
