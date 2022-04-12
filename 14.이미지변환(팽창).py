# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 17:19:50 2022

@author: PC
"""
#팽창 = dilation
#이미지를 확장하여 작은 구멍을 채움
#흰색 영역의 외곽 픽셀 주변에 흰색을 추가

import cv2
import numpy as np

kernel = np.ones((3,3), dtype = np.uint8)

img = cv2.imread('dilate.png', cv2.IMREAD_GRAYSCALE)
dilate1 = cv2.dilate(img, kernel, iterations = 1) #어떤 이미지를 어떤 커널에서, 몇번 반복할 것인가
dilate2 = cv2.dilate(img, kernel, iterations = 2)
dilate3 = cv2.dilate(img, kernel, iterations = 3)

cv2.imshow('gray', img)
cv2.imshow('dilate1', dilate1)
cv2.imshow('dilate2', dilate2)
cv2.imshow('dilate3', dilate3)
cv2.waitKey(0)
cv2.destroyAllWindows()