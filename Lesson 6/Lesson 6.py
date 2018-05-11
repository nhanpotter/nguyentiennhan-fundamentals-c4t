import cv2
import numpy as np

#load Image
I = cv2.imread("D:\\Download by Nhan\\Image\\Lenna.png")
#showimage
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.imshow("Image", I)
#convert Image to grey
grey = cv2.cvtColor(I, cv2.COLOR_RGB2GRAY)
cv2.imshow("grey", grey)
# cv2.waitKey()
# get dimension
# [rows,cols,channel] = Image.shape
print("rgbImage: ", I.shape)
print("greyImage", grey.shape)
[rows, cols] = grey.shape
#
for i in range(rows):
    for j in range(cols):
        # print(grey[i,j],end=" ")
        # grey[i,j] = 0
        if i % 2 == 0 and j % 2 == 0:
            grey[i, j] = 255
    # print("\n")
cv2.imshow("new grey", grey)

#get values
a=[]
[rows1,cols1,channel1]= I.shape
for i in range(rows1):
    for j in range(cols1):
        for k in range(channel1):
            a.append(I[i, j, k])
            if i % 2 == 0 and j % 2 == 0:
                I[i, j, k] = 0
                print(I[i, j, k])
        # print(a,end=" ")
        a=[]
    print("\n")
cv2.imshow("Hello bay be", I)
cv2.waitKey()










