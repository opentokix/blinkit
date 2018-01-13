#!/usr/bin/env python

from blinkt import set_pixel, set_brightness, show, clear
import time


def main():
    set_brightness(0.1)
    for color in range(255):
        for light in range(7):
            set_pixel(light, color, color, color)
            show()
            time.sleep(0.1)

        clear()



if __name__ == '__main__':
    main()