import cv2

cap = cv2.VideoCapture('vid1.mp4')
cv2.namedWindow('Video file')
cv2.namedWindow('blurred')


if __name__ == "__main__":
    ret, img = cap.read()

    while ret:
        blurred = cv2.GaussianBlur(img, (9, 9), 0)
        cv2.imshow('Video file', img)
        cv2.imshow('blurred', blurred)
        cv2.waitKey(10)
        ret, img = cap.read()
