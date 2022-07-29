# Led Maze

A maze generator and solver that displays it in a (hopefully) pretty way through a LED matrix.

This Proof of Concept of the idea is based on Numberphile's video 
["The Lightning Algorithm"](https://www.youtube.com/watch?v=akZ8JJ4gGLs).


### About
The maze generation currently uses Depth-First Search and Breath-First Search to solve it.<br>
Each of the steps in the BFS are used to do the animation.


### Performance

As stated before, I did not focus on performance as this was more of a Proof of Concept of the idea and a way 
to try micropython and the raspberry pi pico. Nevertheless, this is the current performance:

Grid size: 8x8<br>
Sample size: 1000

| delay   | (ms)    |
|---------|---------|
| max     | 2248    |
| min     | 79      |
| average | 389.199 |

2.2 seconds seems like a lot as the worst case, but any animation should take longer than that,
so realistically that never should be a problem.

### Hardware
* **Raspberry Pi Pico**
* **8x8 WS2812B LED matrix**
* **3D Printed Files**:
  * ...