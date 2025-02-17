# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
# SPDX-FileCopyrightText: 2025 Jose David Montoya
# SPDX-License-Identifier: MIT

"""
Basic animations example for LEDSimulation
"""
from machine import Pin
from neoducky import LEDPixel
from animation.solid import Solid
from animation.colorcycle import ColorCycle
from animation.blink import Blink
from animation.comet import Comet
from animation.chase import Chase
from animation.pulse import Pulse
from sequence import AnimationSequence
from Neoducky.colors import (
    PURPLE,
    WHITE,
    AMBER,
    JADE,
    TEAL,
    PINK,
    MAGENTA,
    ORANGE,
)

# Defintions
pixel_num = 30

# Create a NeoPixel ring with 30 pixels connected to pin 15
pixels = LEDPixel(Pin(15), pixel_num)

solid = Solid(pixels, color=PINK)
blink = Blink(pixels, speed=0.5, color=JADE)
colorcycle = ColorCycle(pixels, speed=0.4, colors=[MAGENTA, ORANGE, TEAL])
chase = Chase(pixels, speed=0.1, color=WHITE, size=3, spacing=6)
comet = Comet(pixels, speed=0.01, color=PURPLE, tail_length=10, bounce=True)
pulse = Pulse(pixels, speed=0.1, color=AMBER, period=3)


animations = AnimationSequence(
    # solid,
    # blink,
    # colorcycle,
    # chase,
    # comet,
    pulse,
    advance_interval=5,
    auto_clear=True,
)

while True:
    animations.animate()
