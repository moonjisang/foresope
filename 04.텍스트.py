# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 18:54:45 2022

@author: LG
"""

#opencv에서 사용하는 글꼴 종류
'''cv2.FONT_HERSHEY_SIMPLEX : 보통 크기의 산 세리프 글꼴
cv2.FONT_HERSHEY_PLAIN : 작은 크기의 산 세리프 글꼴
cv2.FONT_HERSHEY_SCRIPT_SIMPLEX : 필기체 스타일 글꼴
cv2.FONT_HERSHEY_TRIPLEX : 보통 크기의 세리프 글꼴
cv2.FONT_ITALIC : 기울임 (이탤릭체)'''

import numpy as np
import cv2

'''img = np.zeros((480, 640, 3), dtype = np.uint8)

SCALE = 1
COLOR = (255, 255, 255)
THICKNESS = 1

cv2.putText(img, 'Nado Simplex', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, SCALE, COLOR, THICKNESS)
#그릴 위치, 텍스트 내용, 시작위치, 폰트 종류, 크기, 색깔, 두께
cv2.putText(img, 'Nado plain', (20, 150), cv2.FONT_HERSHEY_PLAIN, SCALE, COLOR, THICKNESS)
cv2.putText(img, 'Nado script simplex', (20, 250), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, SCALE, COLOR, THICKNESS)
cv2.putText(img, 'Nado triplex', (20, 350), cv2.FONT_HERSHEY_TRIPLEX, SCALE, COLOR, THICKNESS)
cv2.putText(img, 'Nado italic', (20, 450), cv2.FONT_HERSHEY_TRIPLEX | cv2.FONT_ITALIC, SCALE, COLOR, THICKNESS)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

#한글우회방법
#PIL (python image library)
from PIL import ImageFont, ImageDraw, Image

#한글 우회하기 위한 함수
def myPutText(src, text, pos, font_size, font_color):
    img_pil = Image.fromarray(src)
    draw = ImageDraw.Draw(img_pil)
    font = ImageFont.truetype('font/gulim.ttc', font_size)
    draw.text(pos, text, font = font, fill = font_color)
    return np.array(img_pil)

img = np.zeros((480, 640, 3), dtype = np.uint8)

FONT_SIZE = 30
COLOR = (255, 255, 255)


img = myPutText(img, '나도코딩', (20, 50), FONT_SIZE, COLOR)
#그릴 위치, 텍스트 내용, 시작위치, 폰트 종류, 크기, 색깔, 두께

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows