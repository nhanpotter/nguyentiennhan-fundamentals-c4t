import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier("D:\\Download by Nhan\\haarcascade_frontalface_alt2.xml")
mask = cv2.imread("D:\\Download by Nhan\\kitty.jpg")
while True:
    ret, frame = cap.read()

    #convert image to grey
    grey = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    #detect face
    faces = cascade.detectMultiScale(grey)

    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        # newmask = cv2.resize(mask,(w,h),cv2.INTER_CUBIC)
        # frame[y:y+h,x:x+w,:] = frame[y:y+h,x:x+w,:] - newmask
    #careful x: cols ; y: rows
        frame[y:y+h,x:x+w,:] = 0
    cv2.imshow("vid", frame)
    key = cv2.waitKey(30)
    if key==ord("q"):
        break