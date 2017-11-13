# -*- encoding:utf-8 -*-
import socket


class Client(object):

    def __init__(self, ip, port):
        # 创建一个socket:
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 建立连接:
        self.conn.connect((ip, port))

    def __del__(self):
        try:
            if self.conn:
                self.conn.close()
        except Exception as e:
            print e.message
            self.conn = None

    def close(self):
        if self.conn:
            self.conn.close()

    def send(self, data):
        # TODO send data to server
        self.conn.send(bytes(data))
        res = self.recv()
        print res

    def recv(self):
        # TODO recive data from server
        data = []
        while True:
            try:
                d = self.conn.recv(1024)
            except Exception as e:
                print e
                break
            else:
                if d:
                    print d
                    data.append(d)
            if len(d) < 1024:
                print "recv over"
                break
        res = b''.join(data)
        res = res.decode('gbk')
        return res


if __name__ == '__main__':
    c = Client('127.0.0.1', 8888)
    c.recv()
    c.send("ipconfig")
