def gcd(a,b):
  while b:
    a,b = b,a%b
  return a
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
print("GCD of",gcd(num1, num2)) 
