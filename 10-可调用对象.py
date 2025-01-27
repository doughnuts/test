class Cat:

    def eat(self):
        print("吃🐟")

    def __call__(self, *args, **kwargs):
        self.eat()


cat = Cat()
cat()