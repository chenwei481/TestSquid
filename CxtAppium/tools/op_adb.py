#Author:chen
#!/usr/bin/env python
#-*- coding: utf-8 -*-

import subprocess
import os


class AndroidDebugBridge(object):
    def call_adb(self, command):
        command_result = ''
        command_text = 'adb %s' % command
        # print(command_text)
        results = os.popen(command_text, "r")
        while 1:
            line = results.readline()
            if not line: break
            command_result += line
        results.close()
        return command_result

    def attached_devices(self):
        '''重启'''
        # result = self.call_adb("devices")
        devices = []
        result = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE).stdout.readlines()

        for item in result:
            t = item.decode().split("\tdevice")
            if len(t) >= 2:
                devices.append(t[0])
        # print(result)
        # print(devices)
        return devices


    def reboot(self, option):
        '''重启'''
        command = "reboot"
        if len(option) > 7 and option in ("bootloader", "recovery",):
            command = "%s %s" % (command, option.strip())
        self.call_adb(command)

    def push(self, local, remote):
        '''将电脑文件拷贝到手机里面'''
        result = self.call_adb("push %s %s" % (local, remote))
        return result

    def pull(self, remote, local):
        '''拉数据到本地'''
        result = self.call_adb("pull %s %s" % (remote, local))
        return result

    def sync(self, directory, **kwargs):
        '''同步更新 很少用此命名'''
        command = "sync %s" % directory
        if 'list' in kwargs:
            command += " -l"
            result = self.call_adb(command)
            return result

    def open_app(self,packagename,activity):
        '''打开指定app'''
        result = self.call_adb("shell am start -n %s/%s" % (packagename, activity))
        check = result.partition('\n')[2].replace('\n', '').split('\t ')
        if check[0].find("Error") >= 1:
            return False
        else:
            return True

    def get_app_pid(self, pkg_name):
        '''根据包名得到进程id'''
        string = self.call_adb("shell ps | grep "+pkg_name)
        # print(string)
        if string == '':
            return "the process doesn't exist."
        result = string.split(" ")
        # print(result[4])
        return result[4]

    def get_cpu(self,pname):
        '''获取cpu占用'''
        string2 = self.call_adb('shell "dumpsys cpuinfo | grep %s"'%pname)
        res = string2.splitlines()
        for i in res:
            print(i.lstrip())
            if '6933/com.caixuetang.app' in i:
                cpu = i.lstrip()
                return cpu[0:4]


if __name__ == '__main__':
    #AndroidDebugBridge().attached_devices()

    res = AndroidDebugBridge().get_cpu('com.caixuetang.app')
    res = res.splitlines()
    print(res)
