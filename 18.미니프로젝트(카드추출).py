# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 20:40:19 2022

@author: PC
"""

import cv2

img = cv2.imread('card.png')
target_img = img.copy() #사본 이미지

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2. THRESH_OTSU)
contours, hierarchy = cv2.findContours(otsu, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) #이미지, 윤곽선 찾는 모드, 윤곽선 찾을때 사용하는 근사치 방법
#윤곽선 정보, 구조

COLOR = (0, 200, 0) #녹색

idx = 1
for cnt in contours :
    if cv2.contourArea(cnt) > 25000:
        x, y, width, height = cv2.boundingRect(cnt)
        cv2.rectangle(target_img, (x, y), (x+width, y+height), COLOR, 2)
        
        crop = img[y:y+height, x:x+width]
        cv2.imshow(f'card_crop_{idx}', crop)
        cv2.imwrite(f'card_crop_{idx}.png', crop)
        idx += 1



cv2.imshow('img', img)
cv2.imshow('contour', target_img)

cv2.waitKey(0)
cv2.destroyAllWindows()