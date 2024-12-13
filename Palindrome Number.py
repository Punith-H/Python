number = int(input("Enter a number: "))
reverse_number = 0
temp = number

while temp > 0:
    digit = temp % 10
    reverse_number = reverse_number * 10 + digit
    temp // 10

if number == reverse_number:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
