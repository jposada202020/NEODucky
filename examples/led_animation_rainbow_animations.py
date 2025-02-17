# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
# SPDX-FileCopyrightText: Jose David Montoya
# SPDX-License-Identifier: MIT

"""
Rainbow annimations for the LEDSimulation class.
"""
from machine import Pin
from neoducky import LEDPixel
from animation.rainbow import Rainbow
from animation.rainbowchase import RainbowChase
from animation.rainbowcomet import RainbowComet
from animation.rainbowsparkle import RainbowSparkle
from sequence import AnimationSequence

# Defintions
pixel_num = 30

# Create a NeoPixel ring with 30 pixels connected to pin 15
pixels = LEDPixel(Pin(15), pixel_num)


rainbow = Rainbow(pixels, speed=0.1, period=2)
rainbow_chase = RainbowChase(pixels, speed=0.1, size=5, spacing=3)
rainbow_comet = RainbowComet(pixels, speed=0.1, tail_length=7, bounce=True)
rainbow_sparkle = RainbowSparkle(pixels, speed=0.1, num_sparkles=15)


animations = AnimationSequence(
    rainbow,
    rainbow_chase,
    rainbow_comet,
    rainbow_sparkle,
    advance_interval=5,
    auto_clear=True,
)

while True:
    animations.animate()
