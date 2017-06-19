#coding:utf-8
import socket
import json

#开启ip和端口
ip_port = ('127.0.0.1',8888)
#生成一个句柄
sk = socket.socket()
#绑定ip端口
sk.bind(ip_port)
#最多连接数
sk.listen(5)
#开启死循环
def header_handler(mesg):
   print mesg
   dict_obj = json.loads(mesg)
   file_name = dict_obj.get("file_name")
   file_type = dict_obj.get("file_type")
   print "header: ", file_name, file_type
   fp = open(file_name+ "." + file_type, "wb")
   return fp

conn, addr = sk.accept()
header_message = conn.recv(1024)
file_fp = header_handler(str(header_message))
print u'接受键盘消息'
index = 1
while True:
    #获取客户端请求数据
    print index
    index += 1
    print "recv"
    client_data = conn.recv(1024*10)
    if len(client_data) == 0:
        break
    print client_data
    if bytes('\r\nover\r\n') in client_data:
        print "*gggg"
        break
    file_fp.write(client_data)
#关闭链接
print "over"
file_fp.close()
conn.close()
