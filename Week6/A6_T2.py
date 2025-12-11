print("Program starting.")
    
first_name = input("Insert first name: ")
last_name = input("Insert last name: ")
    
filename = input("Insert filename: ")
    
with open(filename, "w") as f:
    f.write(first_name + "\n")
    f.write(last_name + "\n")
    
print("Program ending.")