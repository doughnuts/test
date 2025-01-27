"""
访问控制：
1.私有属性：在属性名前加两个下划线__，只能在类的内部访问，不能在类的外部访问
2.私有方法：在方法名前加两个下划线__，只能在类的内部访问，不能在类的外部访问
3.保护属性：在属性名前加一个下划线_，只能在类的内部访问，不能在类的外部访问，程序员之间不成文规定
"""


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

person=Person("张三",20)
print(person.name)

person.color="red"
print(person.color)