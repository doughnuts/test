"""
__str__:直接输出
__repr__:主要是间接输出，也可以直接输出(当__str__没有重写时)


__len__():len()函数底层调用就是
__del__():垃圾回收调用
__getitem__():使用索引访问元素的时候
__setitem__():索引元素复制的时候
__delitem__():索引删除元素的时候
__iter__():迭代器
__eq__():判断两个对象是否相等
__call__():直接调用对象的时候
"""

class Student:

    def __init__(self,name, age):
        self.name = name
        self.age = age


    def __str__(self):
        return f"姓名：{self.name},年龄：{self.age}"


    def __repr__(self):
        return f"姓名={self.name},年龄={self.age}"


stu=Student("张三",20)
stu1=[stu]
print(stu)
print(stu1)
