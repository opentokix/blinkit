#!/usr/bin/env python

from blinkt import set_pixel, set_brightness, show, clear


def main():
    set_brightness(0.1)
    clear()
    set_pixel(0, 255, 255, 255)
    show()


if __name__ == '__main__':
    main()