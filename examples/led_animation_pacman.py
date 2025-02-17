# SPDX-FileCopyrightText: 2025 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

"""
Pacman example for LEDSimulation
"""
from machine import Pin
from neoducky import LEDPixel
from animation.pacman import Pacman
from colors import WHITE

# Defintions
pixel_num = 30

# Create a NeoPixel ring with 30 pixels connected to pin 15
pixels = LEDPixel(Pin(15), pixel_num)

# Create the Pacman animation object
pacman = Pacman(pixels, speed=0.4, color=WHITE)

# Main loop
while True:
    pacman.animate()
