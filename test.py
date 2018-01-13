#!/usr/bin/env python

from blinkt import set_pixel, set_brightness, show, clear
import time


def main():

    for r in range(255):
        for g in range(255):
            for b in range(255):
                for led in range(8):
                    set_pixel(led, r, g, b)
                    show()
                    time.sleep(0.01)
#        clear()



if __name__ == '__main__':
    main()