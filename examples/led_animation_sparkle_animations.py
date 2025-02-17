# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
This example uses AnimationsSequence to display multiple animations in sequence, at a five second
interval.

For NeoPixel FeatherWing. Update pixel_pin and pixel_num to match your wiring if using
a different form of NeoPixels.
"""
from machine import Pin
from neoducky import LEDPixel

from animation.sparkle import Sparkle
from animation.sparklepulse import SparklePulse
from sequence import AnimationSequence
from colors import PURPLE, JADE

# Defintions
pixel_num = 30

# Create a NeoPixel ring with 30 pixels connected to pin 15
pixels = LEDPixel(Pin(15), pixel_num)


sparkle = Sparkle(pixels, speed=0.1, color=PURPLE, num_sparkles=5)
sparkle_pulse = SparklePulse(pixels, speed=0.15, period=3, color=JADE)

animations = AnimationSequence(
    sparkle,
    sparkle_pulse,
    advance_interval=15,
    auto_clear=True,
)

while True:
    animations.animate()
