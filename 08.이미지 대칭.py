# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 02:25:18 2022

@author: PC
"""

#좌우 대칭
import cv2
'''img = cv2.imread('img.jpg')
flip_horizantal = cv2.flip(img, 1) #flipcode>0 : 좌우대칭

cv2.imshow('img', img)
cv2.imshow('flip_horizantal', flip_horizantal)
cv2.waitKey(0)
cv2.destroyAllWindows()'''


#상하 대칭
img = cv2.imread('img.jpg')
flip_vertical = cv2.flip(img, 0) #flipcode=0 : 상하대칭

cv2.imshow('img', img)
cv2.imshow('flip_vertical', flip_vertical)
cv2.waitKey(0)
cv2.destroyAllWindows()

#상하 좌우 대칭 : flipcode <0