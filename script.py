# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     script
   Description :
   Author :       lishanjie
   date：          2021/10/13
-------------------------------------------------
   Change Activity:
                   2021/10/13:
-------------------------------------------------

"""

__author__ = 'lishanjie'
__time__ = '2021/10/13 15:29'

from appium import webdriver
import time
import util
import threading
from subprocess_demo import AppiumCloud

class OneStorage:

    def __init__(self, address, port, platformVersion='6.0.1', platformName='Android' , deviceName='MuMu'):

        desired_caps = {
            'platformName': platformName,
            'platformVersion': platformVersion,
            'deviceName': deviceName,
            'appPackage': 'com.mobivans.onestrokecharge',
            'appActivity': '.activitys.MainActivity'
        }
        self.driver = webdriver.Remote(f'http://{address}:{port}/wd/hub', desired_caps)
        time.sleep(10)

    def add_recoding(self):

        pos = util.find_image('./tamplate/记一笔.png', './tamplate/main.png')

        self.driver.tap([(pos[0], pos[1])], 10)
        time.sleep(3)
        # driver.save_screenshot('/tamplate/一笔记账.png')

        pos = util.find_image('./tamplate/日常.png', './tamplate/一笔记账tab.png')
        self.driver.tap([(pos[0], pos[1])], 10)

        pos = util.find_image('./tamplate/1.png', './tamplate/点击按钮_1.png')
        self.driver.tap([(pos[0], pos[1])], 10)

        pos = util.find_image('./tamplate/2.png', './tamplate/点击按钮_1.png')
        self.driver.tap([(pos[0], pos[1])], 10)

        pos = util.find_image('./tamplate/point.png', './tamplate/点击按钮_1.png')
        self.driver.tap([(pos[0], pos[1])], 10)

        pos = util.find_image('./tamplate/3.png', './tamplate/点击按钮_1.png')
        self.driver.tap([(pos[0], pos[1])], 10)

        pos = util.find_image('./tamplate/完成.png', './tamplate/点击按钮_1.png')
        self.driver.tap([(pos[0], pos[1])], 10)

        time.sleep(5)

        self.driver.save_screenshot('./tamplate/actul.png')


if __name__ == '__main__':
    # res = AppiumCloud().build_device()
    one = OneStorage('127.0.0.1', '5001', platformVersion='6.0.1', platformName='Android', deviceName='MuMu')
    t1 = threading.Thread(target=one.add_recoding)

    two = OneStorage('127.0.0.1', '5000', platformVersion='9', platformName='Android', deviceName='HUAWEI nova 3')
    t2 = threading.Thread(target=one.add_recoding)

    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()
    t1.join()
    t1.join()