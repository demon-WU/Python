# '''
# 打开文件
# '''
# #w---打开文件，当文件不存在时创建,存在时覆盖
# FileObj=open('./test.txt','w',encoding='utf-8')
# #写文件
# FileObj.write('在苍茫的大海上'*3)
# #关闭文件
# FileObj.close()
# #追加模式------a
# FileObj=open('test.txt','a',encoding='utf-8')
# FileObj.write('这是续作')
# FileObj.close()
# '''
# 以二进制方式去写数据
# '''
# #覆盖式---wb
# FileObj2=open('test1.txt','wb')
# FileObj2.write('这就是Python吗'.encode('utf-8'))
# FileObj2.close()
# #追加模式----ab
# FileObj2=open('test1.txt','ab')
# FileObj2.write('这就是Python吗'.encode('utf-8'))
# FileObj2.close()
# f=open('test.txt','r',encoding='utf-8')
# #读完这段后在继续在后面继续读
# # print(f.read(1))
# # print(f.read())
# #读一行数据-->默认读一行，内有函数定义输入参数读第几个字符
# print(f.readline())
# print(f.readlines(1))
# f1=open('test.txt','rb')
# data=f1.readline().decode('utf-8')
# data=f1.read().decode('utf-8')
# data=f1.readlines().decode('utf-8')
# print(data)
# with open('test.txt','a',encoding='utf-8') as f:
#     f.write('我热爱python\n')
#     pass
with open("test.txt",'rb') as f:
    data=f.read(2)
    print(data.decode('gbk'))
    print(f.tell())
    f.seek(-1,1)
    print(f.tell())