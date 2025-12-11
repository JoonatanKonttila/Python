print("Program starting.\n")
print("Check multiplicative persistence.")

num = int(input("Insert an integer: "))

steps = 0
currentNum = num

while currentNum >= 10:
    digits = [int(dig) for dig in str(currentNum)]
    print(" * ".join(str(dig) for dig in digits), "=", end=" ")
    
    product = 1
    for d in digits:
        product *= d
    
    print(product)
    currentNum = product
    steps += 1

print("No more steps.")
print(f"\nThis program took {steps} step(s)")
print("\nProgram ending.")
