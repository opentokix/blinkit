#!/usr/bin/env python

from blinkt import set_pixel, set_brightness, show, clear
import time

red = [220, 40, 40]
green = [40, 220, 40]
blue = [40, 40, 220]


def main():

    set_pixel(0, blue[0], blue[1], blue[2])
    set_pixel(1, blue[0], blue[1], blue[2])
    set_pixel(2, green[0], green[1], green[2])
    set_pixel(3, green[0], green[1], green[2])
    set_pixel(4, green[0], green[1], green[2])
    set_pixel(5, green[0], green[1], green[2])
    set_pixel(6, red[0], red[1], red[2])
    set_pixel(7, red[0], red[1], red[2])


    show()
    time.sleep(10)



if __name__ == '__main__':
    main()