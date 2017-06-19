# coding: utf-8

import subprocess
import time
from task import send_pic_task
import commands


def screen_shot(file_name='screen_shot', file_type='png'):
    print u'3秒过后第一次截图', file_name, file_type
    # 
    time.sleep(3)
    # 使用subprocess执行其他的程序
    # ret = subprocess.call(["scrot", file_name + '2.' + file_type])
    ret = commands.getstatusoutput("scrot shot2.png")
    print ret
    if ret[0] != 0:
        print u"图片类型不支持，请换用png jpg等常用格式"
        return 
    # 读取图像的二进制文件，进行网络传输
    with open(file_name + '2.' + file_type, "rb") as fp:
        send_pic_task(fp.read(), file_name, file_type)

if __name__ == '__main__':
    screen_shot("shot")

