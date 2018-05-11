import numpy as np
import cv2

# connect webcam
cap = cv2.VideoCapture(0)
lower = np.array([0,30,23])
higher = np.array([137,255,215])

while True:
    ret, frame = cap.read()
    hsvImage = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #convert to binary
    BinImage = cv2.inRange(hsvImage,lower,higher)
    cv2.imshow("hsvImage",hsvImage)


    ret, contours, hierachy = cv2.findContours(BinImage, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for i in range(len(contours)):
        cv2.drawContours(frame, contours, i, (255, 0, 255), 5)
    cv2.imshow("video", frame)
    cv2.imshow("bin", BinImage)
    key = cv2.waitKey(30)
    if key == ord("q"):
        break