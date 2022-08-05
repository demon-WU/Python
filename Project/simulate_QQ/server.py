# 导入套接字模块
import socket
import threading
def handle_request(new_server):
    # 关闭新的套接字
    while True:
        # print(chile_IP)
        revice_data = new_server.recv(1024)
        if revice_data:
            # 接收数据
            # 解码
            revice_new_data = revice_data.decode("UTF-8")
            # 显示数据
            print(revice_new_data)
            pass
        else:
            # print("客户端下线了:".format(chile_IP))
            break
    new_server.close()
if __name__ == '__main__':

    # 设置IPV4，及TCP协议
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 设置连接IP地址及端口号
    # 第一个参数表示IP地址，一般不用指定，表示本机的任何一个IP即可
    # 第二个参数表述端口号
    # 端口号复用
    server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    server_socket.bind(('',9090))
    # 设置监听
    # 128表示最大等待建立连接的个数
    server_socket.listen(128)
    # 创建接收信号
    # 每次当客户端和服务端建立连接成功都会返回一个新的套接字
    # server_socket只负责等待接收客户端的连接请求，收发信息不使用该套接字
    # new_chile 表示新生成的服务器端套接字，收发处理客户端请求
    # server_IP 表示客户端的套接字
    # 循环接收连接请求
    while True:
        new_server,chile_IP = server_socket.accept()
        socket_threading = threading.Thread(target=handle_request,args=(new_server,),daemon=True)
        socket_threading.start()

        # 关闭服务器
        # server_socket.close()