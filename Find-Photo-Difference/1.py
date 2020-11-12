# -*- coding: utf-8 -*-
'''

'''
__author__ = 'Foxlora'
__time__ = '2020/11/12 2:04'

# %%
import win32gui

# %%
import win32con
from PIL import ImageGrab
import numpy as np
import time
import matplotlib.pyplot as plt
import cv2
import itertools
from PIL import ImageChops
import win32api


# %%
game_hwnd = win32gui.FindWindow("#32770", "大家来找茬")
win32gui.ShowWindow(game_hwnd, win32con.SW_SHOWNA)

game_rect = win32gui.GetWindowRect(game_hwnd)

src_image = ImageGrab.grab(game_rect)
# src_image.show()

left_box = (92, 312, 475, 598)
right_box = (512 + 37, 312, 932, 598)

image_left = src_image.crop(left_box)
image_right = src_image.crop(right_box)
# 比较两幅图
diff_image = ImageChops.difference(image_left, image_right)

diff_image.save('diff.jpg', 'jpeg')
# diff_image.show()
# img = plt.imread('images/2.png')
# img = np.uint8(img*255)
# plt.imshow(img)


# %%
img1 = cv2.imread("diff.jpg")
img1 = cv2.medianBlur(img1, 3)
hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)

lower_blue = np.array([0, 0, 0], dtype=np.uint8)
upper_blue = np.array([255, 255, 30], dtype=np.uint8)
mask = cv2.inRange(hsv, lower_blue, upper_blue)
# %%
# 根据阈值构建掩模
kernel = np.ones((1, 1), np.uint8)
contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
list_cnt = []
for cnt in contours:
    area = cv2.contourArea(cnt)
    list_cnt.append({"area": area, "cnt": cnt})
list_cnt.sort(key=lambda obj: obj.get('area'), reverse=True)
for i in range(8):
    x, y, w, h = cv2.boundingRect(list_cnt[i]['cnt'])
    if i < 5:
        dst = cv2.rectangle(img1, (x, y), (x + w, y + h), (255, 0, 0), 2)
        pos = [int(game_rect[0] + left_box[0] + x + w / 2), int(game_rect[1] + left_box[1] + y + h / 2)]
        win32api.SetCursorPos(pos)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    else:
        dst = cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 255, 0), 2)

    time.sleep(1)

# %%



