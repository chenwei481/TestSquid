#Author:chen
#!/usr/bin/env python
#-*- coding: utf-8 -*-
import yaml
from selenium.webdriver.remote.webdriver import WebDriver

class GetCase:

    def __init__(self, path):
        with open(path, 'r', encoding='utf-8') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
        print(data)

    def run(self, driver: WebDriver):
        for step in self.steps:
            element=None
            print(step)

            if isinstance(step, dict):
                if "id" in step.keys():
                    element=driver.find_element_by_id(step["id"])
                elif "xpath" in step.keys():
                    element=driver.find_element_by_xpath(step["xpath"])
                else:
                    print(step.keys())

                if "input" in step.keys():
                    element.send_keys(step["input"])
                else:
                    element.click()

                if "get" in step.keys():
                    text=element.get_attribute(step["get"])
                    print(text)


if __name__ == "__main__":
    getcase = GetCase('D:/Py_test/CxtAppium/data/testDemo.yaml')
