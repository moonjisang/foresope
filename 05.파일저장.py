# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 19:40:51 2022

@author: PC
"""

import cv2

'''img = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE) #흑백으로 불러오기
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

result = cv2.imwrite('img_save.jpg', img) #저장될 파일 이름, 저장할 파일
print(result) #성공시 트루값반환
result = cv2.imwrite('img_save.png', img)''' #png형태로 저장

#동영상 저장
cap = cv2.VideoCapture('video.mp4')
#코덱 정의
fourcc = cv2.VideoWriter_fourcc(*'DIVX') #*을 붙이면 한글자씩 따로 띄어

#프레임 크기, FPS
width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #소수값이 반환될 수도 있으니 반올림
height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS) *2 #영상 재생 속도가 2배

out = cv2.VideoWriter('output.avi', fourcc, fps, (width, height))
#저장 파일 명, 코덱, fps, 크기 (가로, 세로)

while cap.isOpened() :
    ret, frame = cap.read()
    
    if not ret :
        break
    
    out.write(frame) # 영상 데이터만 저장( 소리x )
    cv2.imshow('video', frame)
    if cv2.waitKey(1) == ord('q'):
        break
    
out.release() #자원 해제
cap.release()
cv2.destroyAllWindows()
