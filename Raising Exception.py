def check_age(age):
  age = int(input("Enter your age"))
  if age<18:
    raise ValueError("Age must be greater than 18")
  return True

try:
  check_age(16)
except ValueError as e:
  print(e)
