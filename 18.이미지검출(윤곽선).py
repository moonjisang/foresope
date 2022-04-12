# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 20:10:06 2022

@author: PC
"""

#윤곽선(Contour) : 경계선을 연결한 것

import cv2

'''img = cv2.imread('card.png')
target_img = img.copy() #사본 이미지

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2. THRESH_OTSU)

contours, hierarchy = cv2.findContours(otsu, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) #이미지, 윤곽선 찾는 모드, 윤곽선 찾을때 사용하는 근사치 방법
#윤곽선 정보, 구조
print(hierarchy)
print(f'총 발견 갯수 : {len(contours)}')

COLOR = (0, 200, 0) #녹색
cv2.drawContours(target_img, contours, -1, COLOR, 2) #윤곽선 그리기
#대상 이미지, 윤곽선 정보, 인덱스(-1이면 전체윤곽선), 색깔, 두께

cv2.imshow('img', img)
cv2.imshow('gray', gray)
cv2.imshow('otsu', otsu)
cv2.imshow('contour', target_img)

cv2.waitKey(0)
cv2.destroyAllWindows()


#윤곽선 찾기 모드
#1. cv2.RETR_EXTERNAL : 가장 외곽의 윤곽선만 찾음
#2. cv2.RETR_LIST : 모든 윤곽선 찾음(계층 정보 없음)
#3. cv2.RETR_TREE : 모든 윤곽선 찾음(계층정보를 트리 구조로 생성)'''


#경계 사각형
#윤곽선의 경계면을 둘러싸는 사각형
#boundingRect()

'''img = cv2.imread('card.png')
target_img = img.copy() #사본 이미지

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2. THRESH_OTSU)
contours, hierarchy = cv2.findContours(otsu, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) #이미지, 윤곽선 찾는 모드, 윤곽선 찾을때 사용하는 근사치 방법
#CHAIN_APPROX_NONE : 모든 좌표 반환(윤곽선의), CHAIN_APPROX_SIMPLE : 중복을 제거해서 꼭짓점 좌표만(메모리 줄일수 있음)
#윤곽선 정보, 구조

COLOR = (0, 200, 0) #녹색

for cnt in contours :
    x, y, width, height = cv2.boundingRect(cnt)
    cv2.rectangle(target_img, (x, y), (x+width, y+height), COLOR, 2)



cv2.imshow('img', img)
cv2.imshow('gray', gray)
cv2.imshow('otsu', otsu)
cv2.imshow('contour', target_img)

cv2.waitKey(0)
cv2.destroyAllWindows()'''



#면적
#contourArea()

img = cv2.imread('card.png')
target_img = img.copy() #사본 이미지

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2. THRESH_OTSU)
contours, hierarchy = cv2.findContours(otsu, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) #이미지, 윤곽선 찾는 모드, 윤곽선 찾을때 사용하는 근사치 방법
#윤곽선 정보, 구조

COLOR = (0, 200, 0) #녹색

for cnt in contours :
    if cv2.contourArea(cnt) > 25000:
        x, y, width, height = cv2.boundingRect(cnt)
        cv2.rectangle(target_img, (x, y), (x+width, y+height), COLOR, 2)



cv2.imshow('img', img)
cv2.imshow('contour', target_img)

cv2.waitKey(0)
cv2.destroyAllWindows()