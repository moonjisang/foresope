# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 17:51:46 2022

@author: PC
"""

import cv2

img = cv2.imread('book.jpg', cv2.IMREAD_GRAYSCALE)

ret, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('img', img)
cv2.imshow('binary', binary)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Trackbar(값 변화에 따른 변형 확인)

def empty(pos):
    #print(pos)
    pass

img = cv2.imread('book.jpg', cv2.IMREAD_GRAYSCALE)

name = 'Trackbar'
cv2.namedWindow(name)

cv2.createTrackbar('threshold', name, 127, 255, empty) #bar이름, 창의 이름, 초기값, 최대값, 이벤트 처리

while True:
    thresh = cv2.getTrackbarPos('threshold', name) #bar 이름, 창의 이름
    ret, binary = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)
    
    if not ret:
        break
    
    cv2.imshow(name, binary)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
    
    
'''def empty(pos):
    #print(pos)
    pass

img = cv2.imread('threshold.png', cv2.IMREAD_GRAYSCALE)

name = 'Trackbar'
cv2.namedWindow(name)

cv2.createTrackbar('threshold', name, 127, 255, empty) #bar이름, 창의 이름, 초기값, 최대값, 이벤트 처리

while True:
    thresh = cv2.getTrackbarPos('threshold', name) #bar 이름, 창의 이름
    ret, binary = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)
    
    if not ret:
        break
    
    cv2.imshow('img', img)
    cv2.imshow(name, binary)
    if cv2.waitKey(1) == ord('q'):
        break
    
cv2.destroyAllWindows()'''


'''img = cv2.imread('threshold.png', cv2.IMREAD_GRAYSCALE)

ret, binary1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY) #진한 회색, 밝은 회색, 흰색
ret, binary2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) #밝은 회색 
ret, binary3 = cv2.threshold(img, 195, 255, cv2.THRESH_BINARY) #흰색

cv2.imshow('img', img)
cv2.imshow('binary1', binary1)
cv2.imshow('binary2', binary2)
cv2.imshow('binary3', binary3)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

#Adaptive Threshold, 이미지를 작은 영역으로 나누어서 임계치 적용

'''def empty(pos):
    #print(pos)
    pass

img = cv2.imread('book.jpg', cv2.IMREAD_GRAYSCALE)

name = 'Trackbar'
cv2.namedWindow(name)

#bar이름, 창의 이름, 초기값, 최대값, 이벤트 처리
cv2.createTrackbar('block_size', name, 25, 100, empty)  #홀수만 가능, 1보다는 큰값
cv2.createTrackbar('c', name, 3, 10, empty) #일반적으로 양수의 값을 사용

while True:
    block_size = cv2.getTrackbarPos('block_size', name) #bar 이름, 창의 이름
    c = cv2.getTrackbarPos('c', name)
    
    if block_size <=1:
        block_size = 3
        
    if block_size %2 == 0:
        block_size += 1
    
    binary = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, c)
    

    cv2.imshow(name, binary)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()'''

