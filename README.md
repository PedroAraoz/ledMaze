# Led Maze

A maze generator and solver that displays it in a (hopefully) pretty way through a LED matrix.<br>
This Proof of Concept of the idea is based on Numberphile's video
["The Lightning Algorithm"](https://www.youtube.com/watch?v=akZ8JJ4gGLs).

![leds](https://user-images.githubusercontent.com/22825402/182477022-1cd9cb8b-a2e8-4359-882a-b2876e25b532.gif)

### Table of contents

1. [About](#About)
2. [Instructions](#Instructions)
    1. [Hardware Components](#Hardware-Components)
    2. [Schematic](#Schematic)
    3. [3D Printed Files](#3D-Printed-Files)
    4. [Steps](#Steps)
3. [Performance](#Performance)
3. [Contribution](#Contribution)

### About

The maze generation currently uses Depth-First Search and Breath-First Search to solve it.<br>
Each of the steps in the BFS are used to do the animation.
Then it uses [blaz-r/pi_pico_neopixel](https://github.com/blaz-r/pi_pico_neopixel) library to control the pixels
and try to make some cool patterns.

### Instructions

#### Hardware Components

* **Raspberry Pi Pico**
* **8x8 WS2812B LED matrix**
* **5V power supply**

#### Schematic
![schematic](/images/sketch.png)

#### 3D Printed Files

* ...


#### Steps

1. Clone the repo
2. Connect the Raspberry Pi Pico to your computer
3. Upload `Cell.py`, `Generation.py`, `Maze.py`, `Printer.py`, `Solver.py` to the pico with those names.
   (I recommend using something like [Thonny](https://thonny.org/))
6. Upload [blaz-r/pi_pico_neopixel](https://github.com/blaz-r/pi_pico_neopixel) `neopixel.py`
7. Edit variables in `main.py` if necessary for your specific configuration.
   (If you are copying everything else in these instructions it shouldn't be necessary)
8. Upload `main.py`.
9. Connect the pins according to the schematic.


### Performance

As stated before, I did not focus on performance as this was more of a Proof of Concept of the idea and a way
to try micropython and the raspberry pi pico. Nevertheless, this is the current performance:

Grid size: 8x8<br>
Sample size: 500<br>
Minimum Path Length: 40

| delay   | (ms)     |
|---------|----------|
| max     | 18258    |
| min     | 92       |
| average | 2985.168 |


If the maze generates in less time than the previous animation takes to display it will continue to seamlessly play one
animation after the other. This is because the code utilizes the Pico's multithreading option, so while one core is 
doing the animations,the other is generating the next maze.

Animations usually take around 10 seconds, so a max case of 18 is not ideal.
However, only 17/500 took longer than 10 seconds, so I find that acceptable.
If you never want to have a delay larger than 10s you should probably decrease the minimum path length a bit.



### Contribution

Any contribution to the project is greatly appreciated, just open a PR. 
