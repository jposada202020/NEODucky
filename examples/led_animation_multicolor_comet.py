# SPDX-FileCopyrightText: 2022 Tim Cocks
# SPDX-FileCopyrightText: 2025 Jose David Montoya
# SPDX-License-Identifier: MIT
"""

"""
from machine import Pin
from neoducky import LEDPixel
from animation.multicolor_comet import MulticolorComet

# Defintions
pixel_num = 30

# Create a NeoPixel ring with 30 pixels connected to pin 15
pixels = LEDPixel(Pin(15), pixel_num)

comet_colors = [
    0xFF0000,
    0xFD2000,
    0xF93E00,
    0xF45B00,
    0xEC7500,
    0xE28D00,
    0xD5A200,
    0xC6B500,
    0xB5C600,
    0xA2D500,
    0x8DE200,
    0x75EC00,
    0x5BF400,
    0x3EF900,
    0x20FD00,
    0x00FF00,
]


comet = MulticolorComet(
    pixels,
    colors=comet_colors,
    speed=0.01,
    tail_length=20,
    bounce=True,
    ring=False,
    reverse=False,
)

while True:
    comet.animate()
