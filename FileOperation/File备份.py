def copyFile():
    Original_File=input('请输入你要备份的文件:')
    FileList=Original_File.split('.')
    new_File=FileList[0]+'(备份)'+FileList[1]
    oldFile=open(Original_File,'r',encoding='UTF-8')
    conment=oldFile.read()
    newFile=open(new_File,'w',encoding='UTF-8')
    newFile.write(conment)
    oldFile.close()
    newFile.close()
def copyFilePlus():
    '''
    优化备份功能
    :return:
    '''
    Old_File=input('请输入你要备份的文件:')
    FileList=Old_File.split('.')
    new_File=FileList[0]+'(备份)'+FileList[1]
    try:
        oldFile = open(Old_File, 'r', encoding='UTF-8')
        newFile = open(new_File, 'w', encoding='UTF-8')
        while True:
            conment = oldFile.read(1024)
            newFile.write(conment)
            if len(conment)<1024:
                break
        pass
    except Exception as msg:
        print(msg)
        pass
    finally:
        oldFile.close()
        newFile.close()
        pass
copyFilePlus()