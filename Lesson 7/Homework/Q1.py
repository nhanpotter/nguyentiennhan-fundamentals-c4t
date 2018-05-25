import numpy as np
import cv2

#Load Image RGB
I = cv2.imread("D:\\Download by Nhan\\Image\\shape.jpg")
cv2.imshow("I", I);

cv2.waitKey()
# convert Whiter color to black
[rows, cols, c] = I.shape;
for i in range(rows):
    for j in range(cols):
        if I[i,j,0] >200 and I[i,j,1] >200 and I[i,j,2] >200 :
            I[i,j,:] = 0;
cv2.imshow("Inew", I);
cv2.waitKey()
# Extract chanel B
B = I[:,:,0]
# Extract chanel G
G = I[:,:,1]
# Extract chanel R
R = I[:,:,2]
# Thresold for chanel B
thresh,bin = cv2.threshold(B,200,255,cv2.THRESH_BINARY)
thresh,bin1= cv2.threshold(G,200,255,cv2.THRESH_BINARY)
thresh,bin2= cv2.threshold(R,200,255,cv2.THRESH_BINARY)
a= bin+bin1+bin2
cv2.imshow("binaryImage", a);
cv2.waitKey()

