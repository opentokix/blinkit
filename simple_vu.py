#!/usr/bin/env python
"""Simple program for a vu POC."""

from blinkt import set_pixel, show, clear
import time
import math


def lit(led, color):
    """Set color for pixel."""
    red = [220, 40, 40]
    green = [40, 220, 40]
    blue = [40, 40, 220]

    if color == 'red':
        set_pixel(led, red[0], red[1], red[2])
    if color == 'green':
        set_pixel(led, green[0], green[1], green[2])
    if color == 'blue':
        set_pixel(led, blue[0], blue[1], blue[2])
    if color == 'white':
        set_pixel(led, 255, 255, 255)
    if color == 'dark_grey':
        set_pixel(led, 20, 20, 20)
    if color == 'grey':
        set_pixel(led, 80, 80, 80)
    if color == 'bright_red':
        set_pixel(led, 255, 0, 0)


def update(value):
    """Update the array of leds with some predefined colors."""
    clear()
    if value < 1:
        clear()
    if value == 1:
        lit(0, 'grey')
    if value == 2:
        lit(0, 'grey')
        lit(1, 'blue')
    if value == 3:
        lit(0, 'grey')
        lit(1, 'blue')
        lit(2, 'green')
    if value == 4:
        lit(0, 'grey')
        lit(1, 'blue')
        lit(2, 'green')
        lit(3, 'green')
    if value == 5:
        lit(0, 'grey')
        lit(1, 'blue')
        lit(2, 'green')
        lit(3, 'green')
        lit(4, 'green')
    if value == 6:
        lit(0, 'grey')
        lit(1, 'blue')
        lit(2, 'green')
        lit(3, 'green')
        lit(4, 'green')
        lit(5, 'green')
    if value == 7:
        lit(0, 'grey')
        lit(1, 'blue')
        lit(2, 'green')
        lit(3, 'green')
        lit(4, 'green')
        lit(5, 'green')
        lit(6, 'red')
    if value >= 8:
        lit(0, 'grey')
        lit(1, 'blue')
        lit(2, 'green')
        lit(3, 'green')
        lit(4, 'green')
        lit(5, 'green')
        lit(6, 'red')
        lit(7, 'bright_red')
    show()


def main():
    """Concept code, cos value between 0 and 8."""
    for i in range(1000):
        value = math.cos(float(i) / 10.0) * 4.0 + 4.1
        update(int(value))
        time.sleep(0.01)

if __name__ == '__main__':
    main()
