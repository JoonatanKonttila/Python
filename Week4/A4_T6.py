print("Program starting.")
int1 = int(input("insert a positive integer: "))
collatz = list()
collatz.append(int1)

while int1 != 1:
    if int1 % 2 == 0:
        int1 = int1 // 2
    else:
        int1 = int1 * 3 + 1
    collatz.append(int1)

print(" -> ".join(str(num) for num in collatz))
steps = len(collatz) - 1

print(f"Sequence had", steps, "total steps.")

print("\nProgram ending.")