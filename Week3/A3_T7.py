print("Program starting.")
print("Testing decision structures.")
int1 = int(input("Insert an integer: "))

print("Options: ")
print("1 - In one multi branched decision")
print("2 - In multiple independent if statements")
print("0 - Exit")
choice = int(input("Your choice: "))

if choice == 1:
    if int1 >= 400:
        int1 += 44
    elif int1 >= 200:
        int1 += 22
    elif int1 >= 100:
        int1 += 11
    print("Using one multi-branched decision structure.")
    print(f"Result is {int1}")

elif choice == 2:
    if int1 >= 400:
        int1 += 44
    if int1 >= 200:
        int1 += 22
    if int1 >= 100:
        int1 += 11
    print("Using multiple independent if-statements structure.")
    print(f"Result is {int1}")

elif choice == 0:
    print("Exiting...")

else:
    print("Unknown option.")

print()
print("Program ending.")