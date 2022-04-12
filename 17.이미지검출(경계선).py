# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 19:51:47 2022

@author: PC
"""

#Canny Edge Detection

import cv2
'''img = cv2.imread('snowman.png')

canny = cv2.Canny(img, 150, 200)#대상 이미지, minVal(하위임계값), maxVal(상위임계값)

cv2.imshow('img', img)
cv2.imshow('canny', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()'''




def empty(pos) :
    pass

img = cv2.imread('snowman.png')\
    
name = 'Trackbar'
cv2.namedWindow(name)
cv2.createTrackbar('threshold1', name, 0, 255, empty) #minVal
cv2.createTrackbar('threshold2', name, 0, 255, empty) #maxVal

while True:
    threshold1 = cv2.getTrackbarPos('threshold1', name)
    threshold2 = cv2.getTrackbarPos('threshold2', name)
    
    canny = cv2.Canny(img, threshold1, threshold2)#대상 이미지, minVal(하위임계값), maxVal(상위임계값)    
    cv2.imshow('img', img)
    cv2.imshow(name, canny)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()