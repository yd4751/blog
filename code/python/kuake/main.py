# -*- coding: utf-8 -*-
import os
from bs4 import BeautifulSoup
from kuake import *
from mylog import logger
def loadUrls(source)->list:
    urls = []
    for root, dirs, files in os.walk(source):
        #print(f'当前目录: {root}')
        #print(f'子目录列表: {dirs}')
        #print(f'文件列表: {files}')
        if root != source:
            continue
        for file in files:
            if file.endswith('.html'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    soup = BeautifulSoup(f.read(), 'lxml')
                    for link in soup.find_all('a'):
                        if link.has_attr('href') and link['href'].startswith('https://pan.quark.cn/s/'):
                            urls.append(link['href'])
    return urls

def FileRecord(pos,value=b'0x1'):
    file = 'record.data'
    #read
    if pos is None:
        if not os.path.exists(file):
            return []
        with open(file, 'rb') as f:
            return list(f.read())
    else:
        #write
        file_size = 0
        if os.path.exists(file):
            file_size = os.path.getsize(file)
        with open(file, 'ab') as f:
            if pos > file_size:
                f.write(b'\x01'*(pos-file_size))
            f.seek(pos)
            f.write(value)
'''
urls = loadUrls("ChatExport_2025-03-11/ChatExport_2025-03-11")
with open('urls.txt', 'w', encoding='utf-8') as f:
    for url in urls:
        f.write(url+'\n')
'''

#
pos = 0
urls = []
complete = FileRecord(None)
#
with open('urls.txt', 'r', encoding='utf-8') as f:
    urls = f.readlines()
#
kk = CKuake()
for pos in range(len(urls)):
    url = urls[pos].strip()
    #已完成
    if pos < len(complete) and complete[pos] == 1:
        continue
    try:
        kk.Refresh()
        node = kk.GetShareList(url)
        kk.Save('0',node)
        FileRecord(pos,b'0x1')
    except Exception as e:
        FileRecord(pos,b'0x2')
