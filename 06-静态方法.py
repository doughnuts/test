class Cat:
    def __init__(self):
        ...

    #装饰器
    @staticmethod#静态方法
    def eat():
        print("吃🐟")


cat = Cat()
cat.eat()