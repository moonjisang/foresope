# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 17:04:44 2022

@author: PC
"""

#마우스 이벤트 등록
import cv2
import numpy as np

'''def mouse_handler(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('왼쪽버튼 다운')
        print(x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        print('왼쪽버튼 업')
        print(x, y)
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        print('왼쪽버튼 더블클릭')
    elif event == cv2.EVENT_RBUTTONDOWN:
            print('오른쪽 버튼 다운')
    elif event == cv2.EVENT_MOUSEMOVE:
        print('마우스 이동')


img = cv2.imread('poker.jpg')
cv2.namedWindow('img') #img란 이름의 윈도우를 먼저 만들어두는 것, 여기에 마우스 이벤트를 처리하기 위한 핸들러 적용
cv2.setMouseCallback('img', mouse_handler)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

#프로젝트
point_list = []
src_img = cv2.imread('poker.jpg')

COLOR = (255, 0, 255)

def mouse_handler(event, x, y, flags, param):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        point_list.append((x, y))
        
    for point in point_list:
        cv2.circle(src_img, point, 15, COLOR, cv2.FILLED)
        
    if len(point_list) == 4:
        show_result() #결과 출력
        
    cv2.imshow('img', src_img)
        
    
def show_result():
    
    width, height = 530, 710
    scr = np.float32(point_list)
    dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype = np.float32) #output 4개 지점
    #좌상, 우상, 우하, 좌하(시계방향으로 4지점)

    matrix = cv2.getPerspectiveTransform(scr, dst) #Matrix 얻어옴, 변환 행렬 얻어옴
    result = cv2.warpPerspective(src_img, matrix, (width, height)) #matrix 대로 변환을 함
    cv2.imshow('reslut', result)
    
    
cv2.namedWindow('img') #img란 이름의 윈도우를 먼저 만들어두는 것, 여기에 마우스 이벤트를 처리하기 위한 핸들러 적용
cv2.setMouseCallback('img', mouse_handler)
cv2.imshow('img', src_img)
cv2.waitKey(0)
cv2.destroyAllWindows()