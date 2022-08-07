import socket
if __name__ == '__main__':

    # 创建客户端套接字
    # IPV4类型，TCP协议
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 连接服务器
    client_socket.connect(('192.168.1.2',9090))
    # 发送数据
    data = input('请输入:')
    # 编码
    send_data = data.encode("UTF-8")
    client_socket.send(send_data)
    client_socket.close()