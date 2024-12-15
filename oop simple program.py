class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"hello,my name is {self.name} and I am {self.age} year old")
person1 = Person("alice",35)
person1.greet()
