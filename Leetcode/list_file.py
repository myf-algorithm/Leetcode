# encoding=utf-8

import os
import operator


def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print(files)  # 当前路径下所有非目录子文件
        print(len(files))
        files_dic = {}
        for i in files:
            if i != 'list_file.py' and i != 'a.text':
                i = i.split('.')
                files_dic[int(i[0])] = i[1:]
        print(files_dic)
        files_dic = dict(sorted(files_dic.items(), key=lambda x: x[0]))
        with open('a.text', 'w') as f:
            for key, value in files_dic.items():
                f.write('| ' + str(key) + '.' + str(value[0]) + ' |' + '\n')


file_name('./')
