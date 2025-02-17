# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
# SPDX-FileCopyrightText: 2025 Jose D. Montoya
# SPDX-License-Identifier: MIT

"""
Example of the Chase animation using the LEDSimulation Library.
"""

from machine import Pin
from animation.chase import Chase
from colors import CYAN
from neoducky import LEDPixel


# Defintions
pixel_num = 30

# Create a NeoPixel ring with 30 pixels connected to pin 15
pixels = LEDPixel(Pin(15), pixel_num)

chase = Chase(pixels, speed=0.5, size=4, spacing=6, color=CYAN)

while True:
    chase.animate()
