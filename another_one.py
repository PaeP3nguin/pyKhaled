#!python2

import pyHook
import pythoncom
import pyglet
import time
import ctypes

last_click_time = 0

def onclick(event):
    if event.Message == pyHook.HookConstants.WM_MBUTTONDOWN:
        bless_up.play()
        time.sleep(2)
        ctypes.windll.user32.PostQuitMessage(0)
    else:
        print event.Position
        t = time.time()
        global last_click_time
        print t, last_click_time
        if t > last_click_time + 1.75:
            dj.play()
        else:
            khaled.play()
        last_click_time = t
        return True

dj = pyglet.resource.media('another_one_loud.wav', streaming=False)
khaled = pyglet.resource.media('and_another_one_loud.wav', streaming=False)
bless_up = pyglet.resource.media('bless_up.wav')

hm = pyHook.HookManager()
hm.SubscribeMouseAllButtonsDown(onclick)
hm.HookMouse()
pythoncom.PumpMessages()
hm.UnhookMouse()
