#!/usr/bin/env python

from blinkt import set_pixel, set_brightness, show, clear
import time


def main():
    set_brightness(0.1)
    clear()
    for color in range(255):
        for brightness in range(255):
            set_pixel(brightness, color, color, color)
            show()



if __name__ == '__main__':
    main()