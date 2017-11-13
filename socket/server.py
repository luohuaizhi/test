# -*- encoding:utf-8 -*-
import socket
import threading
import time
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class Server(object):

    def __init__(self, ip='127.0.0.1', port=8888):
        # 创建一个socket:
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 绑定端口
        self.server.bind((ip, port))

    def start(self, max=5):
        # 开始监听(链接数)
        self.server.listen(max)
        # 开始服务，接收链接， 接收消息
        print('Waiting for connection...')
        while True:
            # 接受一个新连接:
            sock, addr = self.server.accept()
            # 创建新线程来处理TCP连接:
            t = threading.Thread(target=tcplink, args=(sock, addr))
            t.start()


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        try:
            if not data or data.decode('utf-8') == 'exit':
                break
            print data
            data = data.decode('utf-8')
            res = execute(data)
            print res
            send(sock, res)
        except Exception as e:
            print e
        finally:
            time.sleep(1)

    sock.close()
    print('Connection from %s:%s closed.' % addr)


def send(sock, message):
    try:
        sock.sendall(message)
    except Exception as e:
        sock.sendall(message.encode('utf-8'))
    finally:
        pass



def execute(cmd):
    p = os.popen(cmd)
    res = p.readlines()
    return b''.join(res)


def main():
    s = Server()
    s.start()


if __name__ == '__main__':
    main()
