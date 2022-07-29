# 导入socket模块
import socket
if __name__ == '__main__':
    while True:
        # socket.AF_INET 为IPV4 ，socket.SOCK_STREAM 为TCP协议
        socket_TCP = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # 连接服务器端
        socket_TCP.connect(('192.168.43.20',9090))
        # 发送信息
        send_data = input('输入你要传达的文字:')
        send_data1 = send_data.encode('UTF-8')
        socket_TCP.send(send_data1)
        # 接收信息
        # recv_data = socket_TCP.recv()
        # recv_data1 = recv_data.decode('UTF-8')
    # 关闭连接
    socket_TCP.close()