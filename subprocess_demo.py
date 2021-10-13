# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     subprocess_demo
   Description :
   Author :       lishanjie
   date：          2021/10/13
-------------------------------------------------
   Change Activity:
                   2021/10/13:
-------------------------------------------------

"""

__author__ = 'lishanjie'
__time__ = '2021/10/13 10:30'

import multiprocessing
import subprocess, os
import socket
import threading
import time
#
# os.system('adb devices')

# devices = subprocess.check_output(['adb', 'devices']).decode().strip().split('\n')
#
# for i in range(1, len(devices)):
#     udid = devices[i].split('\t')[0]
#     print(udid)


class AppiumCloud:

    def find_port(self, port):

        while True:
            if self.check_port(port):
                port += 1
            else:
                break
        return port

    # 检查端口是否被占用
    def check_port(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect(('127.0.0.1', port))
            s.shutdown(2)
        except:
            return False


    def build_device(self):
        list = []
        port = 5000
        bpport = 8000
        devices = subprocess.check_output(['adb', 'devices']).decode('utf-8').strip().split('\n')

        for i in range(1, len(devices)):
            udid = devices[i].split('\t')[0]

            if udid != '':
                version = subprocess.check_output(['adb', '-s', udid,  'shell', 'getprop', 'ro.build.version.release']).decode('utf-8').strip()
                port = self.find_port(port)
                bpport = self.find_port(bpport)

                list.append(str(udid) + ',' + version + ',' + str(port) + ',' + str(bpport))

                bpport += 1
                port += 1
        return list

    def start_appium(self, udid,  version, port, bpport, ):

        command = f'appium -a 0.0.0.0 -p {port} -bp {bpport} --udid {udid} --platform-version {version}'
        os.system(command)
        time.sleep(1)
        print(command)


if __name__ == '__main__':
    ac = AppiumCloud()
    res = ac.build_device()

    processs = []

    for item in res:
        tmp = item.split(',')
        print(tmp)

        processs.append(multiprocessing.Process(target=ac.start_appium, args=(tmp[0], tmp[1], tmp[2], tmp[3])))

    for process in processs:
        process.start()

    for process in processs:
        process.join()



    print("ok")