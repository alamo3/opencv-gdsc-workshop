import cv2

capture = cv2.VideoCapture('rick_roll.mp4')
cv2.namedWindow('video')

face_casecade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


while True:
    ret, frame = capture.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_casecade.detectMultiScale(image=gray, scaleFactor=1.3, minNeighbors = 4, minSize=(160,160), flags = cv2.CASCADE_SCALE_IMAGE)


    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)


    cv2.imshow('video', frame)

    cv2.waitKey(10)


capture.release()
cv2.destroyAllWindows()


