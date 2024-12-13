number = [1,1,2,2,33,33,4,4,5,5,6,6,7,7,8,9]
frequency ={}
for num in number:
  frequency[num]= frequency.get(num,0)+1
print(frequency)
