# 🕹️ Python Raycasting Engine

A basic raycasting engine built with Python and Pygame, simulating 3D graphics using 2D math — inspired by classic games like **Wolfenstein 3D**.

## 🎮 Preview

![Demo GIF](./assets/demo.gif) <!-- (Opsiyonel: varsa bir demo GIF'i burada gösterin) -->

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
