#!/usr/bin/env python

from blinkt import set_pixel, set_brightness, show, clear
import time

step = [ 1, 16, 31, 46, 61, 76, 91, 106, 121, 136, 151, 166, 181, 196, 211, 226, 241, 255 ]

def main():

    for r in step:
        for g in step:
            for b in step:
                for led in range(8):
                    set_pixel(led, r, g, b)
                    show()
#        clear()



if __name__ == '__main__':
    main()