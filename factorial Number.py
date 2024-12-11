num = int(input("enter the number: "))
factorial = 1
for i in range(1, num+1):
  factorial *= i
  print("The factorial is: ", factorial)
