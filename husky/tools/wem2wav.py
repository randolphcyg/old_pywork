# -*- coding: utf-8 -*-
# @Time    : 2019/6/15 3:13
# @Author  : Randolph
# @Email   : cyg0504@outlook.com
# @File    : 移动文件.py
# @Software: PyCharm

import os
import shutil
import time

# Ravioli Scanner（馄饨扫描）将.bytes二进制文件输出为.wem文件格式，命名规范为File000n.wem
# 我们需要删除.dat文件，因为用不到
# Ravioli Extractor（馄饨提取）将上述.wem文件转换为.wav波形文件，
# 每个文件都在File000n.wem文件夹下，命名都是File0001.wav
# 我们需要将文件改名（其文件夹序号）并移到上两层目录、删除空文件夹


def del_dat_file(path):
    """
    删除.dat文件
    :param path: root根目录
    :return:
    """
    for file in os.listdir(path):
        try:
            if os.path.splitext(file)[1] == '.dat':
                print('删除文件', file)
                os.remove(file)
        except:
            print(e)


def del_wem_file(path):
    """
    转换完成后删除.wem文件
    :param path: root根目录
    :return:
    """
    for file in os.listdir(path):
        try:
            if os.path.splitext(file)[1] == '.wem':
                print('删除文件', file)
                os.remove(file)
        except:
            print(e)


def wem2wav(path):
    handle_path = os.path.join(path, '新建文件夹')
    print(handle_path)

    for file in os.listdir(handle_path):
        print(file)
        count = (file.split('.')[0]).split('e')[1]
        f_path = os.path.join(handle_path, file)
        new_wav_name = count + '.wav'

        for f in os.listdir(f_path):
            old_wav_name = f
            print(old_wav_name)
            old_wav_path = os.path.join(f_path, old_wav_name)
            print(old_wav_path)
            new_wav_path = os.path.join(f_path, new_wav_name)
            os.rename(old_wav_path, new_wav_path)
            shutil.move(new_wav_path, handle_path)

    # 删除空文件夹
    for root, dirs, files in os.walk(handle_path, topdown=False):
        if not os.listdir(root):
            os.rmdir(root)


if __name__ == "__main__":
    root = os.getcwd()
    print(root)

    start = time.time()
    del_wem_file(root)      # 删除wem
    end = time.time()
    during2 = end - start
    print('del_wem_file程序运行耗时:%0.2f' % during2)

    wem2wav(root)
