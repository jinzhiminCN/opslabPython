#! /usr/bin/python
# coding=UTF-8
# version:python3.x

from pynput.mouse import Button, Controller
import time

mouse = Controller()

while True:
    time.sleep(3)
    print('The current pointer position is {0}'.format(mouse.position))