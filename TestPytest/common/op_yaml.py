#Author:chen
#!/usr/bin/env python
#-*- coding: utf-8 -*-
import yaml

class OperationYaml():
    def __init__(self,file_adress=None):
        if file_adress != None:
            self.file_adress = '../testdata/yaml/%s.yaml' %file_adress
        else:
            print('没有传yaml文件名称')

    def get_yaml(self):
        '''读取yaml文件数据'''
        with open(self.file_adress,'r',encoding='utf-8') as file:
            yaml_data = yaml.load(file,Loader=yaml.FullLoader)
            #print(yaml_data)
            return yaml_data

    def get_data(self,key):
        '''获取yaml内的具体数据'''
        all_data = self.get_yaml()
        data = all_data[key]
        #print(data)
        return data


if __name__ == '__main__':
    re = OperationYaml('test1')
    re.get_data('test1_1')
