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
    match points:#模式匹配
        case [6,6,_] | [_,6,6]:
            count+=1

print(count)

print("------------------------------")


#名片管理系统

class Card:
    def __init__(self, name, tel, job, addr):
        self.name = name
        self.tel = tel
        self.job = job
        self.addr = addr
