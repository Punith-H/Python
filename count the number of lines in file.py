file_path = "data.txt"

with open(file_path, 'r') as file:
    line_count = sum(1 for line in file)

print(f"Number of lines in the file: {line_count}")
