my_dict = {"Alice": 90, "Bob": 85, "Charlie": 85}
print(my_dict)
rev=dict()
for key,value in my_dict.items():
  rev[value]=key
print(rev)
