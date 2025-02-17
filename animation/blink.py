# SPDX-FileCopyrightText: 2020 Kattni Rembor for Adafruit Industries
# SPDX-FileCopyrightText: 2025 Jose David Montoya
# SPDX-License-Identifier: MIT

"""
`animation.blink`
================================================================================

Blink animation for MicroPython using LEDPixel.

* Author(s): Kattni Rembor

"""

from animation.colorcycle import ColorCycle
from colors import BLACK


class Blink(ColorCycle):
    """
    Blink a color on and off.

    :param pixel_object: The initialised LED object.
    :param float speed: Animation speed in seconds, e.g. ``0.1``.
    :param color: Animation color in ``(r, g, b)`` tuple, or ``0x000000`` hex format.
    :param background_color: Background color in ``(r, g, b)`` tuple, or ``0x000000``
     hex format. Defaults to BLACK.
    :param name: A human-readable name for the Animation. Used by the string function.
    """

    # pylint: disable=too-many-arguments
    def __init__(
        self, pixel_object, speed, color, background_color=BLACK, name=None
    ):
        self._background_color = background_color
        super().__init__(
            pixel_object, speed, [color, background_color], name=name
        )

    def _set_color(self, color):
        self.colors = [color, self._background_color]
