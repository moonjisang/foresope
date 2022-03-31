# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 02:19:44 2022

@author: PC
"""

#영역을 잘라서 새로운 윈도우(창)에 표시
import cv2
'''img = cv2.imread('img.jpg')
print(img.shape)

crop = img[100:200, 200:400] #세로기준 100:200, 가로 기준 200:400까지 자름

cv2.imshow('img', img)
cv2.imshow('crop', crop)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

#영역을 잘라서 기존 윈도우에 표시
img = cv2.imread('img.jpg')


crop = img[100:200, 200:400] #세로기준 100:200, 가로 기준 200:400까지 자름
img[100:200, 400:600] = crop

cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()