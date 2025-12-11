print("Program starting.\n")

startNum = int(input("Insert starting value: "))
stopNum = int(input("Insert stopping value: "))

i = startNum

print("\nStarting while-loop:")

while i < stopNum + 1:
    if i != stopNum + 1:
        print(i, end=" ")
    else:
        print(i, end="")
    i += 1
    
print()    
print("\nProgram ending.")