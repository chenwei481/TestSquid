#Author：chen
# coding=utf-8

import requests
import json

class RunMethon:
    def post_main(self,url,data,header=None):
        res = None
        if header !=None:
            res = requests.post(url=url,data=data,headers=header)
        else:
            res = requests.post(url=url,data=data)
        #print(res.status_code)
        return res.text

    def get_main(self,url,data=None,header=None):
        res = None
        if header != None:
            res = requests.get(url=url, params=data, headers=header)
        else:
            res = requests.get(url=url, params=data)
        #print(res.status_code)
        return res.text

    def run_main(self, method: object, url: object, data: object = None, headers: object = None) -> object:
        res = None
        if method == 'post':
            res = self.post_main(url,data,headers)
        else:
            res = self.get_main(url,data,headers)
        return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=3)

if __name__ == '__main__':
    run = RunMethon()
    run.run_main('get','http://www.apiopen.top/weatherApi?city=%E6%88%90%E9%83%BD')
    #print(requests.get(url='https://www.apiopen.top/weatherApi',params='成都'))