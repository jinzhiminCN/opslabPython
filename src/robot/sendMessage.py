#! /usr/bin/python
# coding=UTF-8
# version:python3.x

"""使用非微信接口定时发送消息，主要针对有些非智障行为的报告"""

from pynput.mouse import Button, Controller
from pynput.keyboard import Key
import pynput
import time

mouse = Controller()
keyboard = pynput.keyboard.Controller()
while True:
    mouse.position = (417, 653)
    #mouse.move(0, 767)
    time.sleep(0.2)
    mouse.press(Button.left)

    keyboard.type('业务正常正常')
    keyboard.press(Key.enter)
    with keyboard.pressed(Key.alt):
        keyboard.press("s")
    time.sleep(2)
