# 导入套接字模块
import socket
if __name__ == '__main__':

    # 设置IPV4，及TCP协议
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 设置连接IP地址及端口号
    # 第一个参数表示IP地址，一般不用指定，表示本机的任何一个IP即可
    # 第二个参数表述端口号
    server_socket.bind(('',9090))
    # 设置监听
    # 128表示最大等待建立连接的个数
    server_socket.listen(128)
    # 创建接收信号
    # 每次当客户端和服务端建立连接成功都会返回一个新的套接字
    # server_socket只负责等待接收客户端的连接请求，收发信息不使用该套接字
    # new_chile 表示新生成的服务器端套接字，收发处理客户端请求
    # server_IP 表示客户端的套接字
    new_chile,server_IP = server_socket.accept()
    print(server_IP)
    # 接收数据
    revice_data = new_chile.recv(1024)
    # 解码
    revice_new_data = revice_data.decode("UTF-8")
    # 显示数据
    print(revice_new_data)
    # 关闭新的套接字
    new_chile.close()
    server_socket.close()