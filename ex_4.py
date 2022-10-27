import cv2
import numpy as np

img = cv2.imread('window.jpeg')

cv2.namedWindow('Original Image')
cv2.namedWindow('Edge detection')

canny_lower = 0
canny_upper = 0


def changeCannyLower(*args):
    global canny_lower
    canny_lower = args[0]


def changeCannyUpper(*args):
    global canny_upper
    canny_upper = args[0]


cv2.createTrackbar('Lower threshold', 'Edge detection', 0, 255, changeCannyLower)
cv2.createTrackbar('Upper threshold', 'Edge detection', 0, 255, changeCannyUpper)


def edge_detection():
    edge = cv2.Canny(img, canny_lower, canny_upper)

    cv2.imshow('Original Image', img)
    cv2.imshow('Edge detection', edge)


if __name__ == "__main__":

    while True:
        edge_detection()
        cv2.waitKey(10)
