file_path = "data.txt"

try:
    with open(file_path, 'r') as file:
        print(f"The file '{file_path}' exists.")
except FileNotFoundError:
    print(f"The file '{file_path}' does not exist.")
