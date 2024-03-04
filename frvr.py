#!/usr/bin/env python

import os
import time

import cv2
import keyboard
import numpy as np

ball = (720, 850)
target = "hoop.png"


def throw_ball(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    os.system(f"xdotool mousemove {x1} {y1} mousedown 1")
    time.sleep(0.2)
    os.system(f"xdotool mousemove {x2} {y2} mouseup 1")


def find_item(img):
    IMG = img
    os.system("maim /tmp/frvr.png")
    img = cv2.imread("/tmp/frvr.png")
    template = cv2.imread(IMG)
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    if len(loc[0]) > 0:
        x = loc[1][0]
        y = loc[0][0]
        n = 0.5
        if x >= 700:
            n = 0.25
        elif x <= 610:
            n = 0.75
        return (x+(template.shape[1]*n), y+(template.shape[0]/2))


def find_speed(img):
    time.sleep(2)
    IMG = img
    os.system("maim /tmp/frvr_1.png")
    time.sleep(0.75)
    os.system("maim /tmp/frvr_2.png")
    img1 = cv2.imread("/tmp/frvr_1.png")
    img2 = cv2.imread("/tmp/frvr_2.png")
    template = cv2.imread(IMG)
    res1 = cv2.matchTemplate(img1, template, cv2.TM_CCOEFF_NORMED)
    res2 = cv2.matchTemplate(img2, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc1 = np.where(res1 >= threshold)
    loc2 = np.where(res2 >= threshold)
    if len(loc1[0]) > 0 and len(loc2[0]) > 0:
        x1 = loc1[1][0]
        y1 = loc1[0][0]
        x2 = loc2[1][0]
        y2 = loc2[0][0]
        x_diff = x2 - x1
        y_diff = y2 - y1
        return (x_diff, y_diff)


def main():
    speed = (0, 0)
    while True:
        if keyboard.is_pressed("esc"):
            break

        time.sleep(1)

        speed = find_speed(target)
        if not speed:
            speed = (0, 0)
        else:
            print(speed)
        hoop = find_item(target)
        if hoop:
            print(hoop)
            hoop = (hoop[0]+speed[0], hoop[1]+speed[1])
            throw_ball(ball, hoop)


if __name__ == "__main__":
    main()
