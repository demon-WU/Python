# 导入socket模块
import socket
if __name__ == '__main__':

    # 创建套接字,IPV4 TCP连接
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 端口号设置
    server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    # 设置端口号
    server_socket.bind(('',9090))
    # 设置监听
    server_socket.listen(128)
    # 设置接收信号函数
    # 将返回新的服务端IP端口号
    new_server,client_IP = server_socket.accept()
    # 接收数据
    recv_data = new_server.recv(1024)
    # 对数据进行解码
    data = recv_data.decode('UTF-8')
    print(data)
    # 关闭临时新的服务端
    new_server.close()
    # 关闭套接字
    server_socket.close()