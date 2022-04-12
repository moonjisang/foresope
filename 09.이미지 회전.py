# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 02:29:37 2022

@author: PC
"""

#이미지 회전
#시계방향 90도 회전
import cv2

'''img = cv2.imread('img.jpg')

rotate_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) #시계방향 90도 회전

cv2.imshow('img', img)
cv2.imshow('img2', rotate_90)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

#180도 회전
'''img = cv2.imread('img.jpg')

rotate_180 = cv2.rotate(img, cv2.ROTATE_180) #시계방향 90도 회전

cv2.imshow('img', img)
cv2.imshow('img2', rotate_180)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

#시계반대 방향 90도 회전(시계방향 270도)
img = cv2.imread('img.jpg')

rotate_270 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE) #시계방향 90도 회전

cv2.imshow('img', img)
cv2.imshow('img2', rotate_270)
cv2.waitKey(0)
cv2.destroyAllWindows()