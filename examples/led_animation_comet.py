# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
# SPDX-FileCopyrightText: 2025 Jose David Montoya
# SPDX-License-Identifier: MIT

"""
Example of the Comet animation using the LEDSimulation Library.
"""
from machine import Pin
from animation.comet import Comet
from colors import JADE, BLUE
from neoducky import LEDPixel


# Defintions
pixel_num = 30

# Create a NeoPixel ring with 30 pixels connected to pin 15
pixels = LEDPixel(Pin(15), pixel_num)


comet = Comet(pixels, speed=0.1, color=BLUE, tail_length=10, bounce=True)

while True:
    comet.animate()
