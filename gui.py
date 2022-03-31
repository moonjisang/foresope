# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 21:57:51 2022

@author: PC
"""

import tkinter as tk # Tkinter
from PIL import ImageTk, Image # Pillow
import cv2 as cv # OpenCV
import os

# GUI 설계
win = tk.Tk() # 인스턴스 생성

win.title("AniWatch") # 제목 표시줄 추가
win.geometry("920x640+50+50") # 지오메트리: 너비x높이+x좌표+y좌표
win.resizable(False, False) # x축, y축 크기 조정 비활성화



frm = tk.Frame(win, bg="white", width=1280, height=720) # 프레임 너비, 높이 설정
frm.grid(row=1, column=0) # 격자 행, 열 배치

lbl1 = tk.Label(frm)
lbl1.grid()


cap = cv.VideoCapture('fire.mp4') # VideoCapture 객체 정의

def video_play():
    ret, frame = cap.read() # 프레임이 올바르게 읽히면 ret은 True
    if not ret:
        cap.release() # 작업 완료 후 해제
        print('error')
        return
    frame = cv.cvtColor(frame, cv.COLOR_BGR2YCrCb)
    img = Image.fromarray(frame) # Image 객체로 변환
    imgtk = ImageTk.PhotoImage(image=img) # ImageTk 객체로 변환
    # OpenCV 동영상
    lbl1.imgtk = imgtk
    lbl1.configure(image=imgtk)
    lbl1.after(10, video_play)

video_play()

win.mainloop() #GUI 시작
