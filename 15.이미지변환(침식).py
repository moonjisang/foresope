# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 19:40:39 2022

@author: PC
"""
#침식 = erosion
#이미지를 깎아서 노이즈 제거
#흰색 영역의 외곽 픽셀을 검은색으로 변형

import cv2
import numpy as np
kernel = np.ones((3,3), dtype = np.uint8)

img = cv2.imread('erode.png', cv2.IMREAD_GRAYSCALE)
erode1 = cv2.erode(img, kernel, iterations = 1)
erode2 = cv2.erode(img, kernel, iterations = 2)
erode3 = cv2.erode(img, kernel, iterations = 3)

cv2.imshow('gray', img)
cv2.imshow('erode1', erode1)
cv2.imshow('erode2', erode2)
cv2.imshow('erode3', erode3)

cv2.waitKey(0)
cv2.destroyAllWindows()