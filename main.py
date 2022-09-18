import os

path = r'填写绝对路径'


def get_filelist(dir):
    Filelist = []
    for home, dirs, files in os.walk(path):
        for filename in files:
            # 文件名列表，包含完整路径
            Filelist.append(os.path.join(home, filename))
            # # 文件名列表，只包含文件名
            # Filelist.append( filename)
    return Filelist


if __name__ == "__main__":
    Filelist = get_filelist(dir)
    #print(len(Filelist))
    for file in Filelist:
        print(file)
        with open(file, 'a') as f:
            f.write('hello md5')
print('修改完成')