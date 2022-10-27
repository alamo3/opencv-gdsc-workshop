import cv2

cap = cv2.VideoCapture('vid1.mp4')

cv2.namedWindow('Video file', cv2.WINDOW_NORMAL)


ret, img = cap.read()

while ret:
    cv2.imshow('Video file', img)

    cv2.waitKey(0)
    ret, img = cap.read()




