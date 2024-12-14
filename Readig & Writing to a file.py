with open("data.txt", "w") as file:
  file.write("Python is awsome!\n")
with open("data.txt", "r") as file:
  content = file.read()
  print(content)
