# SPDX-FileCopyrightText: 2025 Jose D. Montoya
# SPDX-License-Identifier: MIT

"""


"""
from machine import Pin
from neoducky import LEDPixel
from animation.blink import Blink
from colors import BLUE, PURPLE

# Defintions
pixel_num = 30

# Create a NeoPixel ring with 30 pixels connected to pin 15
pixels = LEDPixel(Pin(15), pixel_num)

# Main functiones to test the LEDSimulation object
print(f"Pixels: {pixels}")
print(f"Length of pixels: {len(pixels)}")
print(f"Pixel 0: {pixels[0]}")
print(f"Pixel 1: {pixels[1]}")
print(dir(pixels))

# Create a Blink object
blink = Blink(pixels, speed=0.5, color=PURPLE)

# Run the animation
while True:
    blink.animate()
