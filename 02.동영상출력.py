# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 21:20:34 2022

@author: LG
"""

#동영상 출력

#동영상 파일 출력
'''import cv2
cap = cv2.VideoCapture('video.mp4')

while cap.isOpened():# 동영상 파일이 올바로 열렸는지?
    ret, frame = cap.read()  #ret : 성공여부, frame : 받아온 이미지(프레임)
    if not ret : 
        print('더이상 가져올 프레임이 없어요')
        break
    
    cv2.imshow('video', frame)
    
    if cv2.waitKey(100) == ord('q'):  #key값 비교 위해 ord(아스키 코드로 변환), key값 통해 영상속도 제어 가능
        print('사용자 입력에 의해 종료합니다.')
        break
    
cap.release() #자원해제
cv2.destroyAllWindows()'''

#카메라 출력
import cv2
cap = cv2.VideoCapture(0) # 0번째 카메라 창지(device id)
if not cap.isOpened() :
    exit() #프로그램 종료
    
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    cv2.imshow('camera', frame)
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()