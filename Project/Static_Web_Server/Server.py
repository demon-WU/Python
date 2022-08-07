import socket
import threading
import sys

class webServer(object):
    def __init__(self,port):
        # 设置TCP协议
        TCP_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 端口号复用
        TCP_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 设置端口号
        TCP_socket.bind(('', port))
        # 设置监听
        TCP_socket.listen(128)
        self.TCP_socket = TCP_socket
        pass

    def start(self):
        while True:
            new_socket, IP_socket = self.TCP_socket.accept()
            sub_thread = threading.Thread(target=self.http_test, args=(new_socket,), daemon=True)
            sub_thread.start()

    @staticmethod
    def http_test(new_socket):
        # 接收数据大小
        data = new_socket.recv(4096)
        # 防止客户端发送空数据
        if len(data) == 0:
            return
        # 打印客户端数据
        print(data)
        # 对二进制进行解码
        response_path = data.decode('utf-8')
        # 对客服端发来的请求数据进行分割路径，得出真实请求内容
        new_data_list = response_path.split(' ', 2)
        # 列表类型
        new_data_list_path = new_data_list[1]
        print(new_data_list_path)
        # 追加判断是否是根目录，如果是根目录设置返回的信息
        if new_data_list_path == '/':
            new_data_list_path = '/index.html'
        # 打开文件
        try:
            with open('Static' + new_data_list_path, 'rb') as file:
                file_data = file.read()
                pass
            pass
        except Exception as e:
            # 代码执行到此，说明没有请求的该文件，返回 404 状态码
            # 响应行
            response_line = 'HTTP/1.1 404 OK\r\n'
            # 响应头
            response_header = 'Server: PWS/1.0\r\n'
            with open('Static/404响应.html', 'rb') as file:
                file_data_404 = file.read()
                pass
            # 响应体
            response_body = file_data_404
            # 把数据封装成 HTTP 响应报文格式的数据
            response = (response_line + response_header + '\r\n').encode('utf-8') + response_body
            # 把数据返回到客户端
            new_data = new_socket.send(response)
            pass
        else:
            # 响应行
            response_line = 'HTTP/1.1 200 OK\r\n'
            # 响应头
            response_header = 'Server: PWS/1.0\r\n'
            # 响应体
            response_body = file_data
            # 把数据封装成 HTTP 响应报文格式的数据
            response = (response_line + response_header + '\r\n').encode('utf-8') + response_body
            # 把数据返回到客户端
            new_data = new_socket.send(response)
            pass
        finally:
            # 关闭连接
            new_socket.close()

def main():
    # # 设置命令行启动动态绑定端口号
    # parm = sys.argv
    #
    # # 设置判断至少输入2个参数，且端口号必须为数字
    # if len(parm) != 2:
    #     print('必须输入2个')
    #     return
    # if not parm.isdigit():
    #     print('必须为数字')
    #     return
    # port = int(parm[1])
    http_server = webServer(port)
    http_server.start()
if __name__ == '__main__':
    main()