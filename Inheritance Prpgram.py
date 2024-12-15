class ParentClass:
  def __init__(self,name):
    self.name = name
  
  def name1(self):
    print(f"my name is {self.name}")

class ChildClass(ParentClass):
  def __init__(self,name,age):
    super().__init__(name)
    self.age = age

  def age1(self):
    print(f"my age is {self.age}")

child = ChildClass("alice",30)
child.name1()
child.age1()
