# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 19:44:23 2022

@author: PC
"""

import cv2
import numpy as np

#열림 (Opening) : 침식 후 팽창, 깎아서 노이즈 제거 후 살찌움
# > dilate(erode(img))

kernel = np.ones((3,3), dtype = np.uint8)
img = cv2.imread('erode.png', cv2.IMREAD_GRAYSCALE)

erode = cv2.erode(img, kernel, iterations = 3)
dilate = cv2.dilate(erode, kernel, iterations = 3)


cv2.imshow('img', img)
cv2.imshow('erode', erode)
cv2.imshow('dilate', dilate)
cv2.waitKey(0)
cv2.destroyAllWindows()


#닫힘(Closing) : 팽창 후 침식, 구멍을 메운 후 다시 깎음
#erode(dilate(img))

kernel = np.ones((3,3), dtype = np.uint8)
img = cv2.imread('dilate.png', cv2.IMREAD_GRAYSCALE)

dilate = cv2.dilate(img, kernel, iterations = 3)
erode = cv2.erode(dilate, kernel, iterations = 3)


cv2.imshow('img', img)
cv2.imshow('erode', erode)
cv2.imshow('dilate', dilate)
cv2.waitKey(0)
cv2.destroyAllWindows()