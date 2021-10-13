# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     common
   Description :
   Author :       lishanjie
   date：          2021/9/8
-------------------------------------------------
   Change Activity:
                   2021/9/8:
-------------------------------------------------

"""

__author__ = 'lishanjie'
__time__ = '2021/9/8 22:31'

from appium import webdriver
import time
import os

# package: com.android.chrome

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '6.0.1',
    'deviceName': 'MuMu',
    'appPackage': 'com.mobivans.onestrokecharge',
    'appActivity': '.activitys.MainActivity'
}

driver = webdriver.Remote('http://127.0.0.1:5000/wd/hub', desired_caps)

time.sleep(5)
# driver.find_element_by_id('com.mobivans.onestrokecharge:id/img_wb_back').click()
#
# time.sleep(1)
# driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
#                              'android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
#                              'android.widget.FrameLayout/android.widget.LinearLayout[3]/android.widget.FrameLayout/'
#                              'android.widget.LinearLayout[1]/android.widget.LinearLayout/android.view.View').click()
#
#
# driver.find_element_by_id('com.mobivans.onestrokecharge:id/item_cate_image').click()

# 按键
# com.mobivans.onestrokecharge:id/keyb_btn_0
# com.mobivans.onestrokecharge:id/keyb_btn_1
# com.mobivans.onestrokecharge:id/keyb_btn_2
# com.mobivans.onestrokecharge:id/keyb_btn_3
# com.mobivans.onestrokecharge:id/keyb_btn_4
# com.mobivans.onestrokecharge:id/keyb_btn_5
# com.mobivans.onestrokecharge:id/keyb_btn_6
# com.mobivans.onestrokecharge:id/keyb_btn_7
# com.mobivans.onestrokecharge:id/keyb_btn_8
# com.mobivans.onestrokecharge:id/keyb_btn_9

# com.mobivans.onestrokecharge:id/keyb_btn_dot  .
# com.mobivans.onestrokecharge:id/keyb_btn_del  x
# com.mobivans.onestrokecharge:id/keyb_btn_finish 完成

# driver.swipe(100, 400, 100, 200, 1)
# driver.tap()

width = driver.get_window_size()['width']
height = driver.get_window_size()['height']

print(width, height)
#
# os.system('adb shell screencap -p /storage/emulated/0/main.png')
# time.sleep(2)
# os.system('adb pull /storage/emulated/0/main.png /Users/lishanjie/PycharmProjects/AppDemo/tamplate/main.png')

# driver.save_screenshot('/Users/lishanjie/PycharmProjects/AppDemo/tamplate/main.png')

import util

pos = util.find_image('./tamplate/记一笔.png', './tamplate/main.png')

driver.tap([(pos[0], pos[1])], 10)
time.sleep(3)
# driver.save_screenshot('/tamplate/一笔记账.png')

pos = util.find_image('./tamplate/日常.png', './tamplate/一笔记账tab.png')
driver.tap([(pos[0], pos[1])], 10)

#
# driver.save_screenshot('./tamplate/点击按钮_1.png')

pos = util.find_image('./tamplate/1.png', './tamplate/点击按钮_1.png')
driver.tap([(pos[0], pos[1])], 10)

pos = util.find_image('./tamplate/2.png', './tamplate/点击按钮_1.png')
driver.tap([(pos[0], pos[1])], 10)

pos = util.find_image('./tamplate/point.png', './tamplate/点击按钮_1.png')
driver.tap([(pos[0], pos[1])], 10)

pos = util.find_image('./tamplate/3.png', './tamplate/点击按钮_1.png')
driver.tap([(pos[0], pos[1])], 10)

pos = util.find_image('./tamplate/完成.png', './tamplate/点击按钮_1.png')
driver.tap([(pos[0], pos[1])], 10)

time.sleep(5)

driver.save_screenshot('./tamplate/actul.png')












