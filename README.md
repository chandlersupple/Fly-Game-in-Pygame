Fly-Game-in-Pygame

Controls                                                                                                            
Control 'sprites' with the arrow keys, and change your 'sprite' with the 'a', 's', 'd', and 'w' keys. Press 'b' to spawn a grenade.

Code Explanation                                                                                                                         
Clouds - Using a simple 'if' statement, the clouds loop. A variable 'x', which describes the position of the clouds on the 'x-axis' is increased, then set to 0 when a certain threshold has been met.                                                                           
Bird - The bird's semi-organic motion is the result of a modified sine wave with the function 'y = 100*(sin(0.5*(x)))'. The image itself origionates from the Internet, and is imported when the code is ran.                                                                     
Sprite - Sprites origionate from the Internet, and are controlled via a constant input system which is updates at a rate of 60 frames per seconds (fps).      

Please Note...                                                                                                                             
If running on an older computer, ensure your monitor has a refresh rate of 60 frames per second, as otherwise, the game may appear 'choppy'. Most standard computers are equipped with such equipped with such systems.
