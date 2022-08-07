import multiprocessing
# 跳舞任务
import time


def dance():
    for i in range(3):
        print('跳舞中')
        time.sleep(0.2)
        pass
    pass
def sing():
    for i in range(3):
        print("唱歌中")
        time.sleep(0.2)
        pass
    pass
# 2、创建子进程
# 多线程必须在main函数中执行
if __name__ == '__main__':
    dance_process = multiprocessing.Process(target=dance)
    sing_process = multiprocessing.Process(target=sing)
# 启动进程执行对应的任务
    dance_process.start()
    sing_process.start()
# 执行主进程任务