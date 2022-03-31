# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 16:31:03 2022

@author: LG
"""

'''환경설정
Anaconda prompt에서 다음 명령 수행
pip install opencv-python'''

import cv2


#이미지 출력
'''img = cv2.imread('img.jpg') #해당 경로의 파일 읽어오기
if img is None:
    raise Exception("영상파일 읽기 에러")
cv2.imshow('img', img) #img라는 이름의 창에 img표시
key = cv2.waitKey(0) #지정된 시간동안 사용자 키 입력대기(0)은 무한대기, ()안은 ms단
print(key) #key값은 b(98)처럼 아스키 코드값
cv2.destroyAllWindows() #모든 창 닫기

#읽기 옵션
cv2.IMREAD_COLOR : 컬러 이미지, 투명 영역은 무시(기본값)
cv2.IMREAD_GRAYSCALE : 흑백 이미지
cv2.IMREAD_UNCHANGED : 투명 영역까지 포함

img_color = cv2.imread('img.jpg', cv2.IMREAD_COLOR)
img_gray = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)
img_unchanged = cv2.imread('img.jpg', cv2.IMREAD_UNCHANGED)

cv2.imshow('img1', img_color)
cv2.imshow('img2', img_gray)
cv2.imshow('img3', img_unchanged)

key = cv2.waitKey(0)
cv2.destroyAllWindows()'''

#SHAPE, 이미지의 height, width, channel 정보
img4 = cv2.imread('img.jpg')
print(img4.shape) #세로 가로 채널(RGB)

