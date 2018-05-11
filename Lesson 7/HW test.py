import numpy as np
import cv2

# connect webcam
cap = cv2.VideoCapture(0)
lower = np.array([0,18,0])
higher = np.array([179,255,255])

#cascade
cascade = cv2.CascadeClassifier("D:\\Download by Nhan\\haarcascade_frontalface_alt2.xml")

while True:
    ret, frame = cap.read()
    ret, frame1 = cap.read()

    # cv2.imshow("hsvImage",hsvImage)
    grey = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)

    # cascade
    faces = cascade.detectMultiScale(grey)
    for x, y, w, h in faces:
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 0, 255), 2)
        frame1[y:y + h, x:x + w, :] = 0

    hsvImage = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
    # convert to binary
    BinImage = cv2.inRange(hsvImage, lower, higher)
    #draw contour
    ret, contours, hierachy = cv2.findContours(BinImage, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for i in range(len(contours)):
        cv2.drawContours(frame, contours, i, (255, 0, 255), 5)
        M = cv2.moments(contours[i])
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        cv2.circle(frame, (cx, cy), 10, (120, 255, 0), 5)

    cv2.imshow("video", frame)
    cv2.imshow("bin", BinImage)
    key = cv2.waitKey(30)
    if key == ord("q"):
        break