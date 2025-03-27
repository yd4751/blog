# -*- coding: utf-8 -*-

import json
import copy
from urllib.parse import quote
import time
import requests
import os
from mylog import logger

#
default_cookie = 'b-user-id=0f878cf7-4061-4da6-3be6-c349833a9129; __wpkreporterwid_=20b06b84-9008-467b-1da4-bdeb521debc2; _UP_A4A_11_=wb9c71651a0d4aaaa001ee1df0fae4eb; _UP_30C_6A_=st9c7620138b5qo5ien3t2zcgt3fduhv; _UP_TS_=sg12edca5d7662f3827b25b6754096d40b7; _UP_E37_B7_=sg12edca5d7662f3827b25b6754096d40b7; _UP_TG_=st9c7620138b5qo5ien3t2zcgt3fduhv; _UP_335_2B_=1; __pus=ca767c178c0054a781e8bf4a5fb256d1AAR7imoVS8BS+jNNCQfr7UkciHxpPDDg74EZKeeDj5W8u58igcb5k7Qdnqkj9qWttS5zRdcs0xzyL55RyI6gJPVP; __kp=37640150-ff1d-11ef-9a0d-17a798d97a11; __kps=AAT17ZS1AoLKy4Rnqy0N1O1m; __ktd=0cYr6JLLSFZ0WlFXfmGidw==; __uid=AAT17ZS1AoLKy4Rnqy0N1O1m; __itrace_wid=f9bc5e54-b356-4885-2cfd-827fe0e776ed; ctoken=JIWcSB12Rg-EqdJMyFGYR_Dj; web-grey-id=440aa947-f36a-50a8-5c32-5d64177ef270; web-grey-id.sig=x7F4sqHlz4td95EtY8NmYjseVZfG27L9dKk6jk14myc; grey-id=9254ab42-45e0-7431-e3c9-9ba2fe72bb53; grey-id.sig=Q-SZWW7k5_dGnDYxCEgZEKRQMOzKmOl5qA4as1o-1VY; isQuark=false; isQuark.sig=DWPHMZYiiwQ-v58AbcP-rBdSIpzO8ZnrD67BdJuPatU; b-user-id=0f878cf7-4061-4da6-3be6-c349833a9129; xlly_s=1; __sdid=AASo+xjlDxJGYWcOl2lbbAKxnAo37OoH1sySORRCf92Ys8jkFUHyyDXreC4vxIBzclc=; __chkey=; isg=BMbGpKD43QtT1Ykn8YzQcFClF7xIJwrhJD1XT7DvNOnJs2fNGLaq8VtAj-9_GwL5; tfstk=gx6ERL_2-JeEYvWUrhvr_C41xRJpgp4brTTWqgjkAeYHFWCP_gs4v3_CqU5ySgLHqUqKUY-W061BE32M7FbGAvTWKUmPPg1B-eYHshxXm2xHrkLyjnK5F66P2Y-lqaEpPkF1vMpJErabl-sdv4IqyBXerRcGX3Mo-5OHXoMterabhRNnjLzUlwGYp6Uw2FxHrvD3bVxWqLxHtHqwS3-xZ2bkElrwD3mnrvYkShxvmLYlrLqwInLMrUPFxgDwcBqrgFgZnoskTEjH7xSOQHV6u-LiER6wYG8CxSDoEO-eTTQBjIAyO_jvM9_8UApC01vMcMeEQKjH0wT1o-DwIGsGPICTyx9C7FOVKwzE9efC7IKMs0yvfZTGv9fa2VjhleJHjCw00GAl19dAdPDensIBd_b8GfpFq6vN483Jj6gPe6uoaBx9bEZabXEF4nPNdtsZwbdMHh8bAHG-wBx9bEZabbhJsFKwlktC.; __puus=0240150c2ef089edf0961bdffbedba25AAS41jfbtEtAwfQIO/itXSvwJWcG8lyP89E1f/K/XfKQ+qwHacxKBtsM6VhVmD1SdQB1MuWO7eUd/rJDGBmtyjfu2HlwDKtxdadxBYcSE89gqF5mU069Yn7qRvc46kzSNte7a9U9nW/tt8yNX0GLUNGUPY/onwus+4/Yxw8fLaXecnms3BPsJDu5+B8XfQvNFp45EoVpH6U/GaD7uw6Gzr4x'
default_header = {
    "content-type" : "application/json;charset=UTF-8",
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    #'cookie':
}
default_header['cookie'] = default_cookie
dirType = 0
defaultDir = '临时'
#
def HttpGet(url,body=None,headers=default_header):
    response = None
    if body is not None:
        response = requests.post(url, headers=headers,data=body)
    else:
        response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return response,'[httpGet] {}'.format(response.status_code)
    return response.content,None

def HttpOption(url):
    requests.options(url,headers=default_header)

def GetTimestamp():
    return int(time.time()*1000)
#
class CDirTree:
    def __init__(self,name='root',type=dirType,fid='',token=None):
        self.name = name
        self.type = type
        self.fid = fid
        self.token = token
        self.list = []
    def Add(self,node):
        self.list.append(node)
#
class CKuake:
    def __init__(self):
        self.url = ''
        self.pwd_id = ''
        self.stoken = ''
        self.download_fid = ''
        #
        self.root = CDirTree()
        self._getDir('0',self.root)
    #
    def Refresh(self):
        self.url = ''
        self.stoken = ''
        #移除‘临时’文件夹
        for v in self.root.list:
            if v.type == dirType and v.name == defaultDir:
                self._deleteFile([v.fid])
                return 
    #
    def _getDir(self,dir_fid='0',node:CDirTree=None):
        page = 1
        count = 0
        while True:
            path = "https://drive-pc.quark.cn/1/clouddrive/file/sort?pr=ucpro&fr=pc&uc_param_str=&pdir_fid={0}&_page={1}&_size=50&_fetch_total=1&_fetch_sub_dirs=0&_sort=file_type:asc,updated_at:desc".format(
                dir_fid,page
            )
            result,error = HttpGet(url=path)
            assert error is None,"获取目录失败1"
            page += 1
            result = json.loads(result)
            assert result["status"] == 200,"获取目录失败2"
            
            for v in result["data"]["list"]:
                node.Add(CDirTree(v["file_name"],v["file_type"],v["fid"],v.get('share_fid_token',None)))

            count +=result["metadata"]["_count"]
            if result["metadata"]["_total"] <= count:
                break
        #
        for v in node.list:
            if v.type == dirType:
                self._getDir(v.fid,v)
    #
    def _getSharePage(self,node:CDirTree=None):
        count = 0
        page = 1
        while True:
            path = "https://drive-h.quark.cn/1/clouddrive/share/sharepage/detail?pr=ucpro&fr=pc&uc_param_str=&pwd_id={0}&stoken={1}&pdir_fid=0&force=0&_page={3}&_size=50&_fetch_banner=1&_fetch_share=1&_fetch_total=1&_sort=file_type:asc,updated_at:desc&__dt=2489&__t={2}".format(
                self.pwd_id,quote(self.stoken),GetTimestamp(),page
            )
            result,error = HttpGet(url=path)
            assert error is None,"获取目录失败1"

            result = json.loads(result)
            assert result["status"] == 200,"获取目录失败2"
            
            for v in result["data"]["list"]:
                node.Add(CDirTree(v["file_name"],v["file_type"],v["fid"],v.get('share_fid_token',None)))

            count +=result["metadata"]["_count"]
            if result["metadata"]["_total"] <= count:
                break
            page += 1
        return node
    #
    def _deleteFile(self,fids=[]):
        #option
        path = "https://drive-pc.quark.cn/1/clouddrive/file/delete?pr=ucpro&fr=pc&uc_param_str="
        HttpOption(path)
        #create dir
        path = "https://drive-pc.quark.cn/1/clouddrive/file/delete?pr=ucpro&fr=pc&uc_param_str="
        param = {"action_type":2,"filelist":[],"exclude_fids":[]}
        param["filelist"].extend(fids)
        #tmp_header = copy.copy(default_header)
        #tmp_header["content-type"] = "application/json;charset=UTF-8"
        result,error = HttpGet(url=path,body = json.dumps(param))
        assert error is None,"删除失败"
    #
    def _createDir(self,pdir_fid,dir_name):
        #option
        path = "https://drive-pc.quark.cn/1/clouddrive/file?pr=ucpro&fr=pc&uc_param_str="
        HttpOption(path)
        #create dir
        path = "https://drive-pc.quark.cn/1/clouddrive/file?pr=ucpro&fr=pc&uc_param_str="
        param = {"pdir_fid":pdir_fid,"file_name":"新建文件夹-241018-162054831","dir_path":"","dir_init_lock":False}
        param["file_name"] = dir_name
        #tmp_header = copy.copy(default_header)
        #tmp_header["content-type"] = "application/json;charset=UTF-8"
        result,error = HttpGet(url=path,body = json.dumps(param))
        assert error is None,"创建目录失败"
        result = json.loads(result)
        return result["data"]["fid"]
    #
    def _getToken(self,url):
        self.pwd_id = url[url.rindex('/')+1:]
        path = "https://drive-h.quark.cn/1/clouddrive/share/sharepage/token?pr=ucpro&fr=pc&uc_param_str=&__dt=1920&__t={0}".format(GetTimestamp())
        param = {"pwd_id":"ffce5b8a2175","passcode":""}
        param["pwd_id"] = self.pwd_id
        result,error = HttpGet(url=path,body=json.dumps(param))
        assert error is None,"获取token失败"

        result = json.loads(result)
        return result["data"]["stoken"]
    #
    def GetShareList(self,url)->CDirTree:
        if self.stoken == '':
            self.stoken = self._getToken(url)
        #
        print('[处理分享链接][{}]'.format(url))
        self.url = url
        node = CDirTree("",dirType)
        self._getSharePage(node)
        return node
    #
    def Save(self,pdir_fid,node:CDirTree):
        if pdir_fid == '0':
            pdir_fid = self._createDir(pdir_fid,defaultDir)
            self.download_fid = pdir_fid
        #
        file_list = []
        for v in node.list:
            file_list.append(v)
            '''
            if v['type'] == dirType:
                new_dir_fid = self._createDir(pdir_fid,v['name'])
                v['next'] = CDirTree()
                self.Save(new_dir_fid,v['next'])
            else:
                file_list.append(v)
            '''
        #
        tm = GetTimestamp()
        path = "https://drive-pc.quark.cn/1/clouddrive/share/sharepage/save?pr=ucpro&fr=pc&uc_param_str=&__dt=986004&__t={0}".format(tm)
        HttpOption(path)
        path = "https://drive-pc.quark.cn/1/clouddrive/share/sharepage/save?pr=ucpro&fr=pc&uc_param_str=&__dt=986004&__t={0}".format(tm)
        param = {"fid_list":[],"fid_token_list":[],"to_pdir_fid":"b3faa595feb348238b3359d1a79fabd7","pwd_id":"ffce5b8a2175","stoken":"RJUoMxSK6oI7CQEVznHdCxNhgkBSKu5FmpaG/r/pgxU=","pdir_fid":"0","scene":"link"}
        param["to_pdir_fid"] = pdir_fid
        param["stoken"] = self.stoken
        param["pwd_id"] = self.pwd_id
        for v in file_list:
            param["fid_list"].append(v.fid)
            param["fid_token_list"].append(v.token)
        #
        result,error = HttpGet(url=path,body=json.dumps(param))
        assert error is None,"转存失败1"
        #等待任务完成
        result = json.loads(result)
        assert result["status"] == 200,"转存失败2"
        #
        download_list = []
        task_id = result["data"]["task_id"]
        tryIdx = 0
        while True:
            time.sleep(1)
            path = "https://drive-pc.quark.cn/1/clouddrive/task?pr=ucpro&fr=pc&uc_param_str=&task_id={0}&retry_index={1}&__dt=988551&__t={2}".format(
                task_id,tryIdx,tm
            )
            tryIdx += 1 
            result,error = HttpGet(url=path)
            assert error is None,"获取任务状态失败"

            result = json.loads(result)
            status = result["data"]["status"]
            #if status == 2:
                #download_list.extend(result["data"]["save_as"]["save_as_top_fids"])
                #测试
                #with open("save.json","w",encoding="utf-8") as f:
                #    f.write(json.dumps(result))
                    
            break
        #
        #web端不支持文件夹下载,这里再次获取目录，defaultDir下文件全部下载
        self.total = 0
        self.complete = 0
        self.root = CDirTree()
        self._getDir('0',self.root)
        for v in self.root.list:
            if v.type == dirType and v.name == defaultDir:
                self._download(v,v.name)
        #未完成
        assert self.total > 0 and self.total == self.complete,"未完全下载"
    #
    def _download(self,node,path):
        for v in node.list:
            if v.type == dirType:
                self._download(v,'{0}/{1}'.format(path,v.name))
            else:
                #网页端不支持多文件下载
                self.total += 1
                self._downloadFile(path,[v.fid])
        
    #
    def _downloadFile(self,path,fids,try_count=0):
        if len(fids) == 0:
            return
        if os.path.exists(path) == False:
            os.makedirs(path)
        #
        #
        url = "https://drive-pc.quark.cn/1/clouddrive/file/download?pr=ucpro&fr=pc&uc_param_str="
        HttpOption(url)

        url = "https://drive-pc.quark.cn/1/clouddrive/file/download?pr=ucpro&fr=pc&uc_param_str="
        param = {"fids":[]}
        param["fids"].extend(fids)

        result,error = HttpGet(url=url,body=json.dumps(param))
        #assert error is None,"下载失败1"
        if error is not None:
            try_count += 1
            time.sleep(1*try_count)
            if try_count <= 3:
                self._downloadFile(path,fids,try_count)
            else:
                print('[下载失败1][{0}][{1}][{2}]'.format(path,fids[0],self.url))
                assert False
            return 
        #
        #with open("download.json","w") as f:
        #    f.write(result)
        result = json.loads(result)
        for fileInfo in result["data"]:
            name = fileInfo["file_name"]
            self._ext = name[name.rindex('.')+1:]
            self._name = name[:name.rindex('.')]

            download_url = fileInfo["download_url"]
            md5 = fileInfo["md5"]
            size = fileInfo["size"]
            #
            file_path = "{0}/{1}.{2}".format(path,self._name,self._ext)
            print("正在下载...{0} {1:.2f}M".format(file_path,size/1024/1024))
            #已下载文件跳过
            if os.path.exists(file_path) and size == os.path.getsize(file_path):
                print("文件已存在,跳过")
                self.complete += 1
                continue
            #下载文件
            tmpHeader = copy.copy(default_header)
            tmpHeader.pop("content-type")
            while try_count <= 5:
                self._content,error = HttpGet(url=download_url,headers=tmpHeader)
                if error is not None:
                    try_count += 1
                    time.sleep(1*try_count)
                    if try_count <= 5:
                        continue
                    else:
                        print('[下载失败2][{0}][{1}][{2}]'.format(path,fids[0],self.url))
                        assert False
                        return 
                else:
                    break
            #
            with open(file_path,"wb") as f:
                f.write(self._content)
            self.complete += 1
            try_count = 0
        #休息下，避免被限速
        time.sleep(1)
        return 