def find_second_largest(num):
  if len(num) < 2:
    raise ValueError("The list must contain at least two distinct numbers.")
  largest = second_largest = float('-inf')

  
  for i in num:
    if i > largest: 
      second_largest = largest
      largest = i  
   
    elif i > second_largest and i != largest:  
      second_largest = i  
  
  if second_largest == float('-inf'):
    raise ValueError("The list must contain at least two distinct numbers.")
  return second_largest

numbers = [10, 20, 4, 45, 99, 99]
print("The second-largest number is:", find_second_largest(numbers))
