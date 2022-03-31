# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 16:23:50 2022

@author: PC
"""

#이미지 변형(흐림)
import cv2

#가우시안 블러
#1. 커널 사이즈 변화에 따른 흐림

'''img = cv2.imread('img.jpg')

#(3,3), (5,5), (7,7) 중에 골라쓴다(제일 무난)
kernel_3 = cv2.GaussianBlur(img, (3, 3), 0) #젤 뒤에는 표준편차, 0은 자동
kernel_5 = cv2.GaussianBlur(img, (5, 5), 0)
kernel_7 = cv2.GaussianBlur(img, (7, 7), 0)

cv2.imshow('kernel_3', kernel_3)
cv2.imshow('kernel_5', kernel_5)
cv2.imshow('kernel_7', kernel_7)
cv2.waitKey(0)
cv2.destroyAllWindows()'''


#2. 표준 편차 변화에 따른 흐림

img = cv2.imread('img.jpg')

#(3,3), (5,5), (7,7) 중에 골라쓴다(제일 무난)
sigma_3 = cv2.GaussianBlur(img, (0, 0), 1) #sigma x = 가우시안 커널의 x방향의 표준 편차
sigma_5 = cv2.GaussianBlur(img, (0, 0), 2)
sigma_7 = cv2.GaussianBlur(img, (0, 0), 3)

cv2.imshow('sigma_3', sigma_3)
cv2.imshow('sigma_5', sigma_5)
cv2.imshow('sigma_7', sigma_7)
cv2.waitKey(0)
cv2.destroyAllWindows()
