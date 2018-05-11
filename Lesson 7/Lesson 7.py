import cv2
import numpy as np

I = cv2.imread("D:\\Download by Nhan\\Image\\shape.jpg")
cv2.imshow("load img",I)

#Kênh đọc từ máy tính B-> G-> R
#Extract 3 channels
B = I[:,:,0]
G = I[:,:,1]
R = I[:,:,2]
cv2.imshow("Blue",B)
cv2.imshow("Green",G)
cv2.imshow("Red",R)

#
c_plus=B&G&R
cv2.imshow("New",c_plus)
# convert Image to binary
ret, binImg = cv2.threshold(c_plus,100,255,cv2.THRESH_BINARY_INV)
cv2.imshow("binary",binImg)


#find contour
ret,contours,hierachy = cv2.findContours(binImg,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
# for i in contours:
#     cv2.drawContours(I,i,-1,(255,0,255),5)
# cv2.imshow("Contour",I)
for i in range(len(contours)):
    cv2.drawContours(I,contours,i,(255,0,255),5)
    leni = cv2.arcLength(contours[i],True)
    print("Len of contour: ",leni)
    areai = cv2.contourArea(contours[i])
    print("area contour: ",areai)
    # approximate polygon
    nedges = cv2.approxPolyDP(contours[i],5,True) #5 là sai số của tâm contour đến rìa
    print("polyedges: ", len(nedges))
    if len(nedges) == 3:
        cv2.putText(I,"tam giac", (nedges[2][0][0],nedges[2][0][1]),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0))
    if len(nedges) == 4:
        cv2.putText(I, "Hcn", (nedges[0][0][0], nedges[0][0][1]), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0))
    if len(nedges) >8:
        cv2.putText(I, "Hinh tron", (nedges[0][0][0], nedges[0][0][1]), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0))
    M = cv2.moments(contours[i])
    cx = int(M['m10']/M['m00'])
    # tich phan (x)^i*(y)^j*I(x,y)dx.dy
    #với 'm00' thì i =0, j=0 và tương tự
    #với 'm01' thì i =0, j=1
    cy = int(M['m01']/M['m00'])
    cv2.circle(I,(cx,cy),10,(120,255,0),5)


cv2.namedWindow("New img",cv2.WINDOW_NORMAL)
cv2.imshow("New img",I)
cv2.waitKey()
