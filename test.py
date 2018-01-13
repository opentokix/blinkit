#!/usr/bin/env python

from blinkt import set_pixel, set_brightness, show, clear
import time
import math
import sys

red = [220, 40, 40]
green = [40, 220, 40]
blue = [40, 40, 220]


def update(value):
    if value < 1:
        clear()
    if value == 1:
        set_pixel(0, blue[0], blue[1], blue[2])
    if value == 2:
        set_pixel(0, blue[0], blue[1], blue[2])
        set_pixel(1, blue[0], blue[1], blue[2])
    if value == 3:
        set_pixel(0, blue[0], blue[1], blue[2])
        set_pixel(1, blue[0], blue[1], blue[2])
        set_pixel(2, blue[0], blue[1], blue[2])
    if value == 4:
        set_pixel(0, blue[0], blue[1], blue[2])
        set_pixel(1, blue[0], blue[1], blue[2])
        set_pixel(2, blue[0], blue[1], blue[2])
        set_pixel(3, green[0], green[1], green[2])
    if value == 5:
        set_pixel(0, blue[0], blue[1], blue[2])
        set_pixel(1, blue[0], blue[1], blue[2])
        set_pixel(2, blue[0], blue[1], blue[2])
        set_pixel(3, green[0], green[1], green[2])
        set_pixel(4, green[0], green[1], green[2])
    if value == 6:
        set_pixel(0, blue[0], blue[1], blue[2])
        set_pixel(1, blue[0], blue[1], blue[2])
        set_pixel(2, blue[0], blue[1], blue[2])
        set_pixel(3, green[0], green[1], green[2])
        set_pixel(4, green[0], green[1], green[2])
        set_pixel(5, green[0], green[1], green[2])
    if value == 7:
        set_pixel(0, blue[0], blue[1], blue[2])
        set_pixel(1, blue[0], blue[1], blue[2])
        set_pixel(2, blue[0], blue[1], blue[2])
        set_pixel(3, green[0], green[1], green[2])
        set_pixel(4, green[0], green[1], green[2])
        set_pixel(5, green[0], green[1], green[2])
        set_pixel(6, red[0], red[1], red[2])
    if value >= 8:
        set_pixel(0, blue[0], blue[1], blue[2])
        set_pixel(1, blue[0], blue[1], blue[2])
        set_pixel(2, blue[0], blue[1], blue[2])
        set_pixel(3, green[0], green[1], green[2])
        set_pixel(4, green[0], green[1], green[2])
        set_pixel(5, green[0], green[1], green[2])
        set_pixel(6, red[0], red[1], red[2])
        set_pixel(7, red[0], red[1], red[2])
    show()


def main():
    for i in range(100):
        value = math.sin(i / 5) * 4.0 + 4.0
        sys.stdout.write(str(value))
        sys.stdout.flush()
        update(int(value))
        time.sleep(0.3)


if __name__ == '__main__':
    main()