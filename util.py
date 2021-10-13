# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     util
   Description :
   Author :       lishanjie
   date：          2021/10/12
-------------------------------------------------
   Change Activity:
                   2021/10/12:
-------------------------------------------------

"""

__author__ = 'lishanjie'
__time__ = '2021/10/12 16:25'

# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     demo
   Description :
   Author :       lishanjie
   date：          2021/10/12
-------------------------------------------------
   Change Activity:
                   2021/10/12:
-------------------------------------------------
"""

__author__ = 'lishanjie'
__time__ = '2021/10/12 10:00'

import cv2 as cv
from PIL import ImageGrab


def find_image(target, source):
    target = cv.imread(target)
    source = cv.imread(source)

    result = cv.matchTemplate(source, target, cv.TM_CCORR_NORMED)
    # 返回元组，(0.517378568649292, 0.8508226871490479, (3, 373), (1055, 777)) 包含四个值，
    # 1和3 代表最低匹配度和坐标位置
    # 2和4 代表最高匹配度和坐标位置

    result = cv.minMaxLoc(result)
    # print(target.shape)

    # 计算匹配对象的中心位置x和y
    x = int(result[3][0]) + int(target.shape[1]/2)
    y = int(result[3][1]) + int(target.shape[0]/2)

    if result[1] < 0.95:
        return -1, -1
    else:
        return x, y


if __name__ == '__main__':
    print(find_image('./tamplate/报表.png', './tamplate/记一笔.png'))
