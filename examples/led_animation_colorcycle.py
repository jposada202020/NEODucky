# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
# SPDX-FileCopyrightText: 2025 Jose David Montoya
# SPDX-License-Identifier: MIT

"""
ColorCycle example for LEDSimulation
"""
from machine import Pin
from neoducky import LEDPixel
from animation.colorcycle import ColorCycle
from colors import (
    TEAL,
    MAGENTA,
    ORANGE,
)

# Defintions
pixel_num = 30

# Create a NeoPixel ring with 30 pixels connected to pin 15
pixels = LEDPixel(Pin(15), pixel_num)


colorcycle = ColorCycle(pixels, speed=0.15, colors=[MAGENTA, ORANGE, TEAL])


while True:
    colorcycle.animate()
