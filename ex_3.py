import cv2
import numpy as np

cap = cv2.imread('shapes.png')

cv2.namedWindow('Color Space', cv2.WINDOW_NORMAL)
cv2.namedWindow('Filter', cv2.WINDOW_NORMAL)

hue = 0
hueUpper = 0
sat = 0
satUpper = 0
val = 0
valUpper = 0


def changeHueLow(*args):
    global hue
    hue = args[0]


def changeHueHigh(*args):
    global hueUpper
    hueUpper = args[0]


def changeSatLow(*args):
    global sat
    sat = args[0]


def changeSatHigh(*args):
    global satUpper
    satUpper = args[0]


def changeValLow(*args):
    global val
    val = args[0]


def changeValHigh(*args):
    global valUpper
    valUpper = args[0]


cv2.createTrackbar('Hue Lower', 'Color Space', 0, 179, changeHueLow)
cv2.createTrackbar('Hue Upper', 'Color Space', 0, 179, changeHueHigh)
cv2.createTrackbar('Saturation Lower', 'Color Space', 0, 255, changeSatLow)
cv2.createTrackbar('Saturation Upper', 'Color Space', 0, 255, changeSatHigh)
cv2.createTrackbar('Value Lower', 'Color Space', 0, 255, changeValLow)
cv2.createTrackbar('Value Upper', 'Color Space', 0, 255, changeValHigh)


def create_mask():
    hsv = cv2.cvtColor(cap, cv2.COLOR_RGB2HSV)

    lower_bound = np.array([hue, sat, val])
    upper_bound = np.array([hueUpper, satUpper, valUpper])

    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    cv2.imshow('Color Space', mask)

    img_filter = cv2.bitwise_and(cap, cap, mask=mask)
    cv2.imshow('Filter', img_filter)


create_mask()

while True:
    create_mask()
    cv2.waitKey(10)
