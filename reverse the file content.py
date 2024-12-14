file = open("/content/data.txt","r")
lines = file.readlines()  
a = [line.strip()[::-1] + '\n' for line in lines]  
file.close()

with open("/content/data.txt", "w") as file: 
    file.writelines(a)  
