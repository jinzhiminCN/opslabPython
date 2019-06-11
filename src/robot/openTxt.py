#! /usr/bin/python
# coding=UTF-8
# version:python3.x


from pynput.mouse import Button, Controller
from pynput.keyboard import Key
import pynput
import time

mouse = Controller()
keyboard = pynput.keyboard.Controller()

mouse.position = (0, 767)
#mouse.move(0, 767)
time.sleep(0.2)
mouse.press(Button.left)
time.sleep(0.2)
mouse.move(78, 715)
time.sleep(0.2)
keyboard.type('notepad')
keyboard.press(Key.enter)
time.sleep(2)
keyboard.type('notepad1111111111111')
keyboard.press(Key.enter)
time.sleep(2)

# keyboard.press(Key.enter)
# time.sleep(0.2)
