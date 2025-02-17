# SPDX-FileCopyrightText: Copyright (c) 2025 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

"""

`neodducky`
================================================================================

Micropython library to use Adafruit .

* Author: Jose D. Montoya



"""
from machine import Pin
import rp2
import time
from math import log, e, sin
from colors import BLACK, PURPLE


try:
    from typing import Tuple
except ImportError:
    pass


def color_to_tuple(value: int):
    """Converts a color from a 24-bit integer to a tuple.

    :param value: RGB desired value - can be a RGB tuple or a 24-bit integer.

    """
    if isinstance(value, tuple):
        return value
    if isinstance(value, int):

        if value >> 24:
            raise ValueError("Only bits 0->23 valid for integer input")
        r = value >> 16
        g = (value >> 8) & 0xFF
        b = value & 0xFF
        return [r, g, b]

    raise ValueError("Color must be a tuple or 24-bit integer value.")


def tuple_to_color(rgb_tuple):
    """Converts an RGB tuple to a 24-bit integer.

    :param rgb_tuple: A tuple containing the RGB values.
    :return: A 24-bit integer representing the color.
    """
    if not isinstance(rgb_tuple, tuple) or len(rgb_tuple) != 3:
        raise ValueError("Input must be an RGB tuple with three elements.")

    r, g, b = rgb_tuple
    if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
        raise ValueError(
            "Each element in the RGB tuple must be between 0 and 255."
        )

    return (r << 16) | (g << 8) | b


class LED:
    def __init__(
        self,
        color=0xFFFFFF,
    ) -> None:

        self.r, self.g, self.b = color_to_tuple(color)


class LEDPixel:
    """LEDixel"""

    def __init__(
        self,
        pin: int,
        num_leds: int,
        auto_write=False,
    ):
        self.pin = pin
        self.num_leds = num_leds
        self.leds_list = []
        self.led_color = BLACK
        for _ in range(num_leds):
            self.leds_list.append(LED(self.led_color))
        self._initialize()

    @rp2.asm_pio(
        sideset_init=rp2.PIO.OUT_HIGH,
        out_shiftdir=rp2.PIO.SHIFT_LEFT,
        autopull=True,
        pull_thresh=24,
    )
    def neo_prog():
        """
        PIO program to drive NeoPixels.
        taken from https://toptechboy.com/page/2/ Paul McWhorter
        """
        wrap_target()
        label("bitloop")
        out(x, 1).side(0)
        jmp(not_x, "do_zero").side(1)
        nop().side(1)[5 - 1]
        nop().side(0)[2 - 1]
        jmp("bitloop").side(0)
        label("do_zero")
        nop().side(1)[2 - 1]
        jmp("bitloop").side(0)[6 - 1]
        wrap()

    def _initialize(self) -> None:
        """
        Initialize the NeoPixels state machine.
        :return: None
        """
        self.sm = rp2.StateMachine(
            0,
            self.neo_prog,
            freq=8_000_000,
            sideset_base=Pin(self.pin),
        )
        self.sm.active(1)
        self.fill(PURPLE)

    def ShowNeoPixels(self, led_list) -> None:
        """
        :param pixels: list of pixels
        :return: None
        """
        for color in led_list:
            grb = color.g << 16 | color.r << 8 | color.b  # Green, Red, Blue
            self.sm.put(grb, 8)

    def fill(self, color):
        """
        Cycle through the rainbow colors.
        :param int duration: duration in seconds: default 5 seconds
        :return: None
        """
        for i in range(self.num_leds):
            self.leds_list[i] = LED(color)

    def show(self):
        self.ShowNeoPixels(self.leds_list)

    def __repr__(self):
        return [(led.r, led.g, led.b) for led in self.leds_list]

    def __iter__(self):
        return iter(self.leds_list)

    def __getitem__(self, index):
        return (
            self.leds_list[index].r,
            self.leds_list[index].g,
            self.leds_list[index].b,
        )

    def __len__(self):
        return len(self.leds_list)

    def get_color_position_in_palette(self, color):
        if color not in self.palette:
            self.palette[self._palette_counter] = color
            self._palette_helper.append(color)
            color_position_in_palette = self._palette_counter
            self._palette_counter += 1
        else:
            color_position_in_palette = self._palette_helper.index(color)
        return color_position_in_palette

    def set_led_color(self, led, color):
        led.r, led.g, led.b = color

    def __setitem__(self, index, color):

        if isinstance(color, int):
            converted_color = color_to_tuple(color)

            self.set_led_color(
                self.leds_list[index],
                converted_color,
            )

        elif len(color) == 3 and isinstance(color, tuple):
            converted_color = tuple_to_color(color)

            self.set_led_color(self.leds_list[index], color)

        else:
            for index, element in enumerate(color):
                if element == 0:
                    self.set_led_color(self.leds_list[index], (0, 0, 0))

                elif isinstance(element, int):
                    converted_color = color_to_tuple(element)

                    self.set_led_color(self.leds_list[index], converted_color)

                else:
                    converted_color = tuple_to_color(element)

                    self.set_led_color(self.leds_list[index], element)
