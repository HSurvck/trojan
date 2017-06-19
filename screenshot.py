# coding: utf-8
import os
import time
from task import send_pic_task
import commands


def screen_shot(file_name='screen_shot', file_type='png'):
    """
    本程序未实现指定图片存储的路径，用户自行实现该扩展功能
    借助os.path.join函数
    """
    print u'3秒过后第一次截图', file_name, file_type
    time.sleep(3)
    # 调用外部程序
    ret = commands.getstatusoutput("scrot " + file_name + '.' + file_type)
    if ret[0] != 0:
        print u"图片类型不支持，请换用png jpg等常用格式"
        return
    # 读取图像的二进制文件，进行网络传输
    with open(file_name + 'tmp.' + file_type, "rb") as fp:
        send_pic_task(fp.read(), file_name, file_type)
    os.remove(file_name + '.' + file_type)
    print u'发送屏幕截图完成'


if __name__ == '__main__':
    screen_shot("shot")
