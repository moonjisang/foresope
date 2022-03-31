# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 21:40:21 2022

@author: LG
"""

#도형 그리기

#빈스케치북 만들기
import cv2
import numpy as np

#세로 480, 가로 640, 3채널(RGB)에 해당하는 스케채북 만들기
'''img = np.zeros((480, 640, 3), dtype = np.uint8)
#img[:] = (0, 255, 0) #전체 공간을 흰 색으로 채우기, (b g r 순서)
#print(img)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

#일부 영역 색칠
'''img = np.zeros((480, 640, 3), dtype = np.uint8)
img[100:200, 200:300] = (255, 255, 255) #세로영역, 가로영역
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

#직선
#직선의 종류 (line type)
#1. cv2.LINE_4 : 상하좌우 4방향으로 연결된 선
#2. cv2.LINE_8 : 대각선을 포함한 8방향으로 연결된 선(기본값)
#3. CV2.LINE_AA : 부드러운 선 (anti-aliasing)

'''img = np.zeros((480, 640, 3), dtype = np.uint8)
COLOR = (0, 255, 255) #yellow
THICKNESS = 3 # 두께

cv2.line(img, (50, 100), (400, 50), COLOR, THICKNESS, cv2.LINE_8)
#그릴 위치, 시작,끝점, 색깔, 두께, 선 종류
cv2.line(img, (50, 200), (400, 50), COLOR, THICKNESS, cv2.LINE_4)
cv2.line(img, (50, 300), (400, 50), COLOR, THICKNESS, cv2.LINE_AA)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

#원그리기
'''img = np.zeros((480, 640, 3), dtype = np.uint8)
COLOR = (255, 255, 0) #yellow
RADIUS = 50 # 반지름
THICKNESS = 10

cv2.circle(img, (200, 100), RADIUS, COLOR, THICKNESS, cv2.LINE_AA) # 속이 빈 원
#그릴 위치, 원의 중심, 반지름, 색깔, 두께, 선 종류
cv2.circle(img, (400, 100), RADIUS, COLOR, cv2.FILLED, cv2.LINE_AA)#속이 꽉 찬 원, -1대신 써도 됨

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

#사각형
'''img = np.zeros((480, 640, 3), dtype = np.uint8)
COLOR = (0, 255, 0) #yellow
THICKNESS = 3

cv2.rectangle(img, (100, 100), (200, 200), COLOR, THICKNESS) #속이 빈 사각형

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

#다각형
img = np.zeros((480, 640, 3), dtype = np.uint8)
COLOR = (0, 0, 255) #red
THICKNESS = 3

pts1 = np.array([[100, 100], [200, 100], [100, 200]])
pts2 = np.array([[200, 100], [300, 100], [300, 200]])
cv2.polylines(img, [pts1, pts2], True, COLOR, THICKNESS, cv2.LINE_AA) #true, false는 끝점과 시작점을
#잇냐 안잇냐 차이, 닫힘, 열림차이

pts3 = np.array([[[100, 300], [200, 300], [100, 400]], [[200, 300], [300, 300], [300, 400]]])
cv2.fillPoly(img, pts3, COLOR, cv2.LINE_AA)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()