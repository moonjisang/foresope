# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 00:28:30 2022

@author: PC
"""

#이미지

#고정 크기로 설정
import cv2
'''img = cv2.imread('img.jpg')
dst = cv2.resize(img, (400, 500)) #width, height 고정 크기

cv2.imshow('img', img)
cv2.imshow('resize', dst)
cv2.waitKey(0)
cv2.dsetroyAllWindows()'''

#비율로 설정
'''img = cv2.imread('img.jpg')
dst = cv2.resize(img, None, fx = 0.5, fy = 0.5) #x y 비율 정의(0.5배로 축소)

cv2.imshow('img', img)
cv2.imshow('resize', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

#보간법
#cv2.INTER_AREA : 크기 줄일 때 사용
#cv2.INTER_CUBIC : 크기 늘릴 때 사용(속도 느림, 퀄리티 좋음)
#cv2.INTER_LINEAR : 크기 늘릴 때 사용(기본 값)
'''img = cv2.imread('img.jpg')
dst = cv2.resize(img, None, fx = 1.5, fy = 1.5, interpolation = cv2.INTER_CUBIC)

cv2.imshow('img', img)
cv2.imshow('resize', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

#동영상

#고정 크기로 설정
'''cap = cv2.VideoCapture('video.mp4')

while cap.isOpened() :
    ret, frame = cap.read()
    if not ret :
        break
    
    frame_resize = cv2.resize(frame, (1000, 500))
    
    cv2.imshow('video', frame_resize)
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()'''
        
#비율로 설정
cap = cv2.VideoCapture('video.mp4')

while cap.isOpened() :
    ret, frame = cap.read()
    if not ret :
        break
    
    frame_resize = cv2.resize(frame, None, fx = 1.5, fy = 1.5, interpolation = cv2.INTER_CUBIC)
    
    cv2.imshow('video', frame_resize)
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()