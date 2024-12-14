try:
  num = int(input("Enter the Number: "))
  print(10/num)
except ZeroDivisionError:
  print("YOu can't divide by zero")
except ValueError:
  print("Invalid Input")
