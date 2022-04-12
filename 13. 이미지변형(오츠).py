# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 16:22:32 2022

@author: PC
"""

#오츠 알고리즘
#bimodal image에 사용하기 적합(최적의 임계치를 자동으로발견)
import cv2

img = cv2.imread('book.jpg', cv2.IMREAD_GRAYSCALE)

ret, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) #진한 회색, 밝은 회색, 흰색
ret, otsu = cv2.threshold(img, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print('otsu threshold', ret)

cv2.imshow('img', img)
cv2.imshow('binary', binary)
cv2.imshow('otsu', otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()
