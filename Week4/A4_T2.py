#two int for loop

print("Program starting.\n")

startNum = int(input("Insert starting value: "))
stopNum = int(input("Insert stopping value: "))

print("")

print("Starting for-loop:")

for i in range(startNum, stopNum + 1):
    if i != stopNum:
        print (i, end=" ")
    else:
        print(i, end="")

print("\nProgram ending.")