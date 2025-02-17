# SPDX-FileCopyrightText: 2025 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

"""
Solid example for LEDSimulation
"""
from machine import Pin
from neoducky import LEDPixel
from animation.solid import Solid
from colors import PINK

# Defintions
pixel_num = 30

# Create a NeoPixel ring with 30 pixels connected to pin 15
pixels = LEDPixel(Pin(15), pixel_num)

solid = Solid(pixels, color=PINK)

while True:
    solid.animate()
