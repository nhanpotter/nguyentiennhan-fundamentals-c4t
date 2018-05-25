import numpy
import cv2

I = cv2.imread("D:\\Download by Nhan\\Image\\erosion.jpg")
cv2.imshow("Initial",I)
cv2.waitKey()
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))

bin_erode = cv2.erode(I,kernel)
bin = cv2.dilate(bin_erode,kernel)
cv2.imshow("Bin",bin)
cv2.waitKey()
