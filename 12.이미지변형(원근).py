# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 16:36:28 2022

@author: PC
"""
#사다리꼴 이미지 펼치기
import cv2
import numpy as np

img = cv2.imread('paper.jpg')

width, height = 640, 240 #가로크기 640, 세로크기 240으로 결과물 출력

scr = np.array([[511, 352], [1008, 345], [1112, 584], [455, 594]], dtype = np.float32) #imput 4개 지점
dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype = np.float32) #output 4개 지점
#좌상, 우상, 우하, 좌하(시계방향으로 4지점)

matrix = cv2.getPerspectiveTransform(scr, dst) #Matrix 얻어옴, 변환 행렬 얻어옴
result = cv2.warpPerspective(img, matrix, (width, height)) #matrix 대로 변환을 함

cv2.imshow('img', img)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()



'''img = cv2.imread('poker.jpg')

width, height = 530, 710

scr = np.array([[702, 143], [1133, 414], [726, 1007], [276, 700]], dtype = np.float32) #imput 4개 지점
dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype = np.float32) #output 4개 지점
#좌상, 우상, 우하, 좌하(시계방향으로 4지점)

matrix = cv2.getPerspectiveTransform(scr, dst) #Matrix 얻어옴, 변환 행렬 얻어옴
result = cv2.warpPerspective(img, matrix, (width, height)) #matrix 대로 변환을 함

cv2.imshow('img', img)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()'''