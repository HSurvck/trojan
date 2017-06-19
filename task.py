# coding: utf-8
import socket
import json
import time

"""
课程实现了
"""

SERVER_CONFIG = {
    "IP": "127.0.0.1",
    "PORT": 8888,
}


class NetworkClient(object):
    def __init__(self, config):
        self.server_ip = config['IP']
        self.server_port = config['PORT']
        self.sock = socket.socket()
        self.sock.connect((self.server_ip, self.server_port))

    def send_data(self, data):
        print "send network success: "
        ret = self.sock.sendall(data)
        assert ret != -1

    def destroy(self):
        try:
            self.sock.close()
        except Exception as e:
            print e
            


class BasicNetworkTask(object):
    def __init__(self, server_instance, content):
        self.server = server_instance
        self.content = content

    def run(self):
        self.server.send_data(self.content)


class NetworkTaskManager(object):

    def __init__(self, server_instance, file_type, file_name):
        self.server_instance = server_instance
        self.file_type = file_type
        self.file_name = file_name

        self.send_message_header()

    def send_message_header(self):
        header_message = {
            "file_name": self.file_name,
            "file_type": self.file_type
        }
        task = BasicNetworkTask(self.server_instance, json.dumps(header_message))
        task.run()

    def send_content(self, content):
        task = BasicNetworkTask(self.server_instance, content)
        task.run()
        return "success"

    def send_stop_message(self):
        content = "\r\nover\r\n"
        task = BasicNetworkTask(self.server_instance, content)
        task.run()
        self.server_instance.destroy()


def send_pic_task(content, file_name='screenshot', file_type='png'):
    server = NetworkClient({"IP": "127.0.0.1", 'PORT': 8889})
    obj = NetworkTaskManager(server, file_type=file_type, file_name=file_name)
    print "cahngdu", len(content)
    time.sleep(1)
    obj.send_content(content)
    obj.send_stop_message()
