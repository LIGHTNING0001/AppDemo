# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     adb_command
   Description :
   Author :       lishanjie
   date：          2021/10/12
-------------------------------------------------
   Change Activity:
                   2021/10/12:
-------------------------------------------------

"""

__author__ = 'lishanjie'
__time__ = '2021/10/12 17:37'


import os, time

# os.system('adb shell screencap -p /storage/emulated/0/main.png')
# time.sleep(2)
# os.system('adb pull /storage/emulated/0/main.png /Users/lishanjie/PycharmProjects/AppDemo/tamplate/main.png')

os.system('adb shell am start com.mobivans.onestrokecharge/.activitys.MainActivity')

time.sleep(10)
import util
pos = util.find_image('./tamplate/记一笔.png', './tamplate/main.png')
os.system(f'adb shell input tap {pos[0]} {pos[1]}')

pos = util.find_image('./tamplate/日常.png', './tamplate/一笔记账tab.png')
os.system(f'adb shell input tap {pos[0]} {pos[1]}')

pos = util.find_image('./tamplate/1.png', './tamplate/点击按钮_1.png')
os.system(f'adb shell input tap {pos[0]} {pos[1]}')


pos = util.find_image('./tamplate/2.png', './tamplate/点击按钮_1.png')
os.system(f'adb shell input tap {pos[0]} {pos[1]}')

pos = util.find_image('./tamplate/point.png', './tamplate/点击按钮_1.png')
os.system(f'adb shell input tap {pos[0]} {pos[1]}')

pos = util.find_image('./tamplate/3.png', './tamplate/点击按钮_1.png')
os.system(f'adb shell input tap {pos[0]} {pos[1]}')

pos = util.find_image('./tamplate/完成.png', './tamplate/点击按钮_1.png')
os.system(f'adb shell input tap {pos[0]} {pos[1]}')

time.sleep(10)

os.system('adb shell screencap -p /storage/emulated/0/actul.png')
time.sleep(2)
os.system('adb pull /storage/emulated/0/actul.png /Users/lishanjie/PycharmProjects/AppDemo/tamplate/actul.png')