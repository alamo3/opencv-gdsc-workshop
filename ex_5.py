import cv2

capture = cv2.VideoCapture(0)
cv2.namedWindow('video', cv2.WINDOW_NORMAL)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


while True:
    ret, frame = capture.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    faces = face_cascade.detectMultiScale(image=gray, minSize=(180, 180), flags=cv2.CASCADE_SCALE_IMAGE)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    cv2.imshow('video', frame)

    cv2.waitKey(10)