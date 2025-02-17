# SPDX-FileCopyrightText: 2020 Kattni Rembor for Adafruit Industries
# SPDX-FileCopyrightText: 2025 Jose David Montoya
# SPDX-License-Identifier: MIT

"""
`animation.colorcycle`
================================================================================

Color cycle animation for MicroPython using LEDPixel.

* Author(s): Kattni Rembor

"""

from animation import Animation
from colors import RAINBOW


class ColorCycle(Animation):
    """
    Animate a sequence of one or more colors, cycling at the specified speed.

    :param pixel_object: The initialised LED object.
    :param float speed: Animation speed in seconds, e.g. ``0.1``.
    :param colors: A list of colors to cycle through in ``(r, g, b)`` tuple, or ``0x000000`` hex
                   format. Defaults to a rainbow color cycle.
    :param start_color: An index (from 0) for which color to start from. Default 0 (first color).
    """

    # pylint: disable=too-many-arguments
    def __init__(
        self, pixel_object, speed, colors=RAINBOW, name=None, start_color=0
    ):
        self.colors = colors
        self.start_color = start_color
        super().__init__(pixel_object, speed, colors[start_color], name=name)
        self._generator = self._color_generator(start_color)
        next(self._generator)

    on_cycle_complete_supported = True

    def draw(self):
        self.pixel_object.fill(self.color)
        next(self._generator)

    def _color_generator(self, start_color):
        index = start_color
        while True:
            self._color = self.colors[index]
            yield
            index = (index + 1) % len(self.colors)
            if index == start_color:
                self.cycle_complete = True

    def reset(self):
        """
        Resets to the first color.
        """
        self._generator = self._color_generator(self.start_color)
