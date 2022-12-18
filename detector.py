#!/usr/bin/env python
# coding=utf-8

import numpy as np
import time
import cv2


def arrow_detect():
    cascader2Straight = cv2.CascadeClassifier("cascade2Straight.xml")
    cascader2Right = cv2.CascadeClassifier("cascade2Right.xml")
    cascader2Left = cv2.CascadeClassifier("cascade2Left.xml")
    if cascader2Straight.empty():
        print("couldn't load straight")
    if cascader2Right.empty():
        print("couldn't load right")
    if cascader2Left.empty():
        print("couldn't load left")
    cap = cv2.VideoCapture(0)

    counter_s = 0
    counter_r = 0
    counter_l = 0
    while (cap.isOpened()):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)
        #gray = cv2.GaussianBlur(gray, (5, 5), 0)
        #gray = cv2.Canny(gray, 50, 150)

        straight = cascader2Straight.detectMultiScale(
            gray, 1.1, 2, 0, (10, 10))
        right = cascader2Right.detectMultiScale(gray, 1.1, 2, 0, (10, 10))
        left = cascader2Left.detectMultiScale(gray, 1.1, 2, 0, (10, 10))
        # straight = np.array(straight)
        # right = np.array(right)
        # left = np.array(left)

        if len(straight) > 0:
            for (x, y, w, h) in straight:
                #roi_gray = gray[y:y+h, x:x+w]
                frame = cv2.rectangle(
                    frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                counter_s += 1
                counter_r = 0
                counter_l = 0
                # print("straight")
                X, Y, width, hieght = x, y, w, h
                mid_x, mid_y = (x+(x+w))/2, (y+(y+h))/2
        elif len(right) > 0:
            for (x, y, w, h) in right:
                #roi_gray = gray[y:y+h, x:x+w]
                frame = cv2.rectangle(
                    frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                counter_r += 1
                counter_s = 0
                counter_l = 0
                # print("right")
                X, Y, width, hieght = x, y, w, h
                mid_x, mid_y = (x+(x+w))/2, (y+(y+h))/2
        elif len(left) > 0:
            for (x, y, w, h) in left:
                #roi_gray = gray[y:y+h, x:x+w]
                frame = cv2.rectangle(
                    frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                counter_l += 1
                counter_s = 0
                counter_r = 0
                # print("left")
                X, Y, width, hieght = x, y, w, h
                mid_x, mid_y = (x+(x+w))/2, (y+(y+h))/2
        if counter_s >= 10:
            print("straight")
            counter_s = 0
            print(X, Y, width, hieght, mid_x, mid_y)
        if counter_r >= 10:
            print("right")
            counter_r = 0
            print(X, Y, width, hieght, mid_x, mid_y)
        if counter_l >= 10:
            print("left")
            counter_l = 0
            print(X, Y, width, hieght, mid_x, mid_y)

        cv2.imshow("frame", frame)
        key = cv2.waitKey(1)
        # ESC
        if key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
    return counter_s, counter_r, counter_l, X, Y, width, hieght


counter_s, counter_r, counter_l, X, Y, width, hieght = arrow_detect()
