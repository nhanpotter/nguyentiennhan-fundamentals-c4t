import cv2
import numpy as np

# create capture
cap = cv2.VideoCapture(0)
# nếu video thì trong"" ghi đường link

#Show video
while(True):
    ret,img = cap.read()
    print(ret)

    cv2.imshow("video",img)
    key = cv2.waitKey(30)
    if key == ord("q"):
        break
