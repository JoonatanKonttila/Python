print("Program starting\n")

print("Options:")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")
choice = int(input("Your choice: "))

if choice == 1:
    C1 = float(input("Insert the amount of Celsius: "))
    fahr = round(C1 * 1.8 + 32, 1)
    print(f"{C1} °C equals to {fahr} °F")
elif choice == 2:
    C2 = float(input("Insert the amount of Fahrenheit: "))
    cels = round((C2 - 32) / 1.8, 1)
    print(f"{C2} °F equals to {cels} °C")
elif choice == 0:
    print("Exiting...")
else:
    print("Unknown option.")

print()
print("Program ending.")