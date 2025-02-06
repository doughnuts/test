class Student:
    name="zhangsan"
    age=20

    def __new__(cls, *args, **kwargs):
        for i in range(0,10):
            print("haha")
        return 11

stu1=Student()
print(stu1)



print("---------------------------------")


import random
count=0
for j in range(100):
    points=[random.randint(1,6) for i in range(3)]#列表推导式
    print(points)
    match points:#模式匹配
        case [6,6,_] | [_,6,6]:
            count+=1

print(count)

print("------------------------------")











#多线程读取json和yaml

import threading
import json
import yaml
import time

class JsonRead(threading.Thread):
    def __init__(self, file_name, thread_name):
        super().__init__()
        self.file_name = file_name
        self.name = thread_name

    def run(self):
        time.sleep(1)
        with open(self.file_name, mode="rt", encoding="utf-8") as f:
            obj = json.load(f)
            print(obj)


class YamlRead(threading.Thread):
    def __init__(self, file_name, thread_name):
        super().__init__()
        self.file_name = file_name
        self.name = thread_name

    def run(self):
        with open(self.file_name, mode="rt", encoding="utf-8") as f:
            obj = yaml.safe_load(f)
            print(obj)

j = JsonRead("a.json", "json")
y = YamlRead("a.yaml", "yaml")

j.start()
# j.join()
y.start()
