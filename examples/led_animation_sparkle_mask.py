# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries, karan bhatia
# SPDX-FileCopyrightText: 2025 Jose D. Montoya
# SPDX-License-Identifier: MIT
"""
Sparkle Animation Example for NeoDisplay
"""
from machine import Pin
from neoducky import LEDPixel

from animation.sparkle import Sparkle
from sequence import AnimationSequence
from colors import JADE, AQUA, PINK

# Defintions
pixel_num = 64

# Update to match the number of NeoPixels you have connected

# fmt: off
heart_mask = [     1,  2,          5,  6,
              8,   9, 10, 11, 12, 13, 14, 15,
              16, 17, 18, 19, 20, 21, 22, 23,
              24, 25, 26, 27, 28, 29, 30, 31,
                  33, 34, 35, 36, 37, 38,
                      42, 43, 44, 45,
                          51, 52]
unheart_mask = [0,           3,  4,         7,



                32,                        39,
                40, 41,                46, 47,
                48, 49, 50,        53, 54, 55,
                56, 57, 58, 59, 60, 61, 62, 63]
# fmt: on
# Create a NeoPixel ring with 30 pixels connected to pin 15
pixels = LEDPixel(Pin(15), pixel_num)

animations = AnimationSequence(
    Sparkle(pixels, speed=0.05, color=JADE, num_sparkles=1, mask=unheart_mask),
    Sparkle(pixels, speed=0.05, color=AQUA, num_sparkles=1),
    Sparkle(pixels, speed=0.05, color=PINK, num_sparkles=1, mask=heart_mask),
    advance_interval=5,
    auto_clear=True,
)

while True:
    animations.animate()
