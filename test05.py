class Dog:
    name = "大黑狗"
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def look_door(self):
        print("看门",self)



dog=Dog("小黑狗",12)
print(Dog.name)
print(dog.name)
print(dog.age)
print(dog.look_door)
