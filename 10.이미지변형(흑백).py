# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 16:18:14 2022

@author: PC
"""

#이미지 변형(흑백)



import cv2
#흑백으로 불러옴
'''img = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

img = cv2.imread('img.jpg')

dst = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #불러온 이미지를 흑백으로 변경
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()