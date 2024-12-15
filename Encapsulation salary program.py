class person:
  def __init__(self,name,age):
    self.name = name
    self.age = age
    self.__salary = 5000

  def get_salary(self):
    return self.__salary

  def set_salary(self,new_salary):
    self.__salary = new_salary

  def set_salary(self,new_salary):
    if new_salary > 0:
      self.__salary = new_salary
    else:
      print("salary must be positive")

  def dispaly_info(self):
    print(f"name: {self.name}, age: {self.age}, salary: {self.__salary}")

perso = person("alice",30)
perso.dispaly_info()
perso.set_salary(6000)
perso.dispaly_info()
