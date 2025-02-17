# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries,
# SPDX-FileCopyrightText: 2025 Jose David Montoya
# SPDX-License-Identifier: MIT

"""
CustomColorChase example for LEDSimulation
"""
from machine import Pin
from neoducky import LEDPixel
from animation.customcolorchase import CustomColorChase
from sequence import AnimationSequence
from colors import PINK, GREEN, RED, BLUE
from rainbow import rainbow_colors

# Defintions
pixel_num = 30

# Create a NeoPixel ring with 30 pixels connected to pin 15
pixels = LEDPixel(Pin(15), pixel_num)

# colors default to RAINBOW as defined in color.py
custom_color_chase_rainbow = CustomColorChase(
    pixels, speed=0.5, size=2, spacing=3
)
custom_color_chase_rainbow_r = CustomColorChase(
    pixels, speed=0.1, size=3, spacing=3, reverse=True
)

# Example with same colors as RainbowChase
steps = 30

# Now use rainbow_colors with CustomColorChase
custom_color_chase_rainbowchase = CustomColorChase(
    pixels, speed=0.3, colors=rainbow_colors, size=2, spacing=3
)

custom_color_chase_bgp = CustomColorChase(
    pixels, speed=0.3, colors=[BLUE, GREEN, PINK], size=3, spacing=2
)

# Can use integer values for color, 0 is black
custom_color_chase_br = CustomColorChase(
    pixels, speed=0.1, colors=[BLUE, 0, RED, 0], size=2, spacing=0
)

animations = AnimationSequence(
    custom_color_chase_rainbow,
    custom_color_chase_rainbow_r,
    custom_color_chase_rainbowchase,
    custom_color_chase_bgp,
    custom_color_chase_br,
    advance_interval=6,
    auto_clear=True,
)

while True:
    animations.animate()
