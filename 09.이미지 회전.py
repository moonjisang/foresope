# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 02:29:37 2022

@author: PC
"""

#이미지 회전
#시계방향 90도 회전
import cv2
img = cv2.imread('img.jpg')

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()