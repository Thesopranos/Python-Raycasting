# 🕹️ Python Raycasting Engine

A basic raycasting engine built with Python and Pygame, simulating 3D graphics using 2D math — inspired by classic games like **Wolfenstein 3D**.

## 🚀 Features

- Basic raycasting algorithm with 2D maps
- Simulated 3D rendering via vertical slice projection
- Minimalistic and easy-to-understand structure
- Wall collisions and player movement
- Written purely in Python using the Pygame library

## 🧠 How It Works

This project simulates 3D perspective using a **2D grid map** and **ray casting** to detect walls. Each "ray" checks for intersections with the environment and renders vertical lines based on distance — giving the illusion of depth.

## 📦 Requirements

- Python 3.x
- Pygame

Install dependencies:

```bash
pip install pygame
```

### Key	Action  
W / S => Move forward / backward  
A / D =>	Strafe left / right  
← / → Arrows => Rotate view left / right  


### 🗺️ Sample Map
The game uses a 2D grid to define the world.
In the grid:

1 = Wall

0 = Empty space

python
Kopyala
Düzenle
```bash
MAP = [
    [1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,1],
    [1,0,1,0,1,0,0,1],
    [1,0,1,0,0,0,0,1],
    [1,0,0,0,1,0,0,1],
    [1,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1]
]
```
### 📁 Project Structure
.  
├── maps  
├──── map1.map - # map example 1  
├──── map2.map - # map example 1  
├── src  
├──── map.py  ----      # 2D map definition and handling  
├── main.py  -------        # Main loop and game logic  
└── README.md  -- # Documentation (this file)  
