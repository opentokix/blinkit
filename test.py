#!/usr/bin/env python

from blinkt import set_pixel, set_brightness, show, clear
import time

red = [200, 40, 40]
green = [ 40, 200, 40]
blue = [40, 40, 200]



def main():

    set_pixel(0, red[0], red[1], red[2])
    show()
    time.sleep(10)



if __name__ == '__main__':
    main()