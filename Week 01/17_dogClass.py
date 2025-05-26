class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def detail(self):
        return f'{self.name} is {self.age} year old.'

dog1 = Dog('Bruno',5)
print(dog1.detail())            