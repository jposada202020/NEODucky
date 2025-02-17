# SPDX-FileCopyrightText: 2025 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

"""
Pulse example for LEDSimulation
"""
from machine import Pin
from neoducky import LEDPixel
from animation.pulse import Pulse
from colors import AMBER

# Defintions
pixel_num = 30

# Create a NeoPixel ring with 30 pixels connected to pin 15
pixels = LEDPixel(Pin(15), pixel_num)

pulse = Pulse(pixels, speed=0.1, color=AMBER, period=3)

while True:
    pulse.animate()
