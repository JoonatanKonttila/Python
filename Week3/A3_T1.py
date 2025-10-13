print("Program starting.")
print("Insert two integers.")
int1 = int(input("Insert first integer: "))
int2 = int(input("Insert second integer: "))

print("Comparing inserted integers.")

if int1 == int2:
    print("Integers are the same.\n")
elif int1>int2:
    print("First integer is greater.\n")
else:
    print("Second integer is greater.\n")

print("Adding integers together")
sum = int1+int2
print(f"{int1} + {int2} = {sum}\n")

print("Checking the parity of the sum...")

if sum % 2 != 0:
    print("Sum is odd.")
else:
    print("Sum is even")
print("Program ending.")