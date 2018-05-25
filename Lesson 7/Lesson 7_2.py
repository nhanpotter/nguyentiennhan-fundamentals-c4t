import numpy as np
import cv2

# def timGTmax(b):
#     GTmax = b[0]
#     for i in range(len(b)):
#         if b[i] >= max:
#             GTmax = i
#     return GTmax


# connect webcam
cap = cv2.VideoCapture(0)
lower = np.array([0,28,11])
higher = np.array([179,221,255])

while True:
    ret, frame = cap.read()

    frame = cv2.flip(frame,1)
    cv2.rectangle(frame,(int(frame.shape[1]/2),0),(int(frame.shape[1]),int(3*(frame.shape[0]/4))),(0,0,255),5)

    roi = frame[5:int(3*(frame.shape[0]/4))-5,5+int(frame.shape[1]/2):int(frame.shape[1])-5,:]

    hsvImage = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
    #convert to binary
    BinImage = cv2.inRange(hsvImage,lower,higher)
    cv2.imshow("hsvImage",hsvImage)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))

    bin_erode = cv2.erode(BinImage, kernel)

    ret, contours, hierachy = cv2.findContours(bin_erode, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for i in contours:
        cv2.drawContours(roi, i,-1, (255, 0, 255), 5)
    if len(contours) >0:
        maxlen = cv2.arcLength(contours[0],True)
        indexmax = 0
        for i in range(len(contours)):
            leni = cv2.arcLength(contours[i],True)
            if leni > maxlen:
                maxlen = leni
                indexmax = i
        cv2.drawContours(roi, contours, indexmax,(0,0,255),5)

        M = cv2.moments(contours[indexmax])
        if M['m00'] != 0:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            cv2.circle(roi, (cx, cy), 10, (120, 255, 0), 5)



    cv2.imshow("video", frame)
    # cv2.imshow("bin", bin_erode)
    cv2.imshow("roiImage",roi)
    key = cv2.waitKey(30)
    if key == ord("q"):
        break

