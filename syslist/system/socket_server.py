# file:socket_server.py
# desc:socket
# auth:Carol Luo

import socket

class socket_server:
    #套接字字段
    __socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    #本机主机名
    __host   = scoket.gethostname()
    #监听端口号
    __port   = 0

    #构造函数
    def __init__(self, port, listen):
        #绑定端口
        self.__socket.bind((host, port))
        #最大监听
        self.__socket.listen(listen)
    
    #析构函数
    def __del__(self)
        __socket = __socket
        __socket.close()