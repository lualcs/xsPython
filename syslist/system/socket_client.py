# file:socket_client.py
# desc:socket
# auth:Carol Luo

import socket

class socket_client:
    #套接字字段
    __socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    #构造函数
    def __init__(self, host, port):
        __socket = self.__socket
        #网络连接
        __socket.connect(host, port)
    
    #析构函数
    def __del__(self)
        __socket = self.__socket
        __socket.close()