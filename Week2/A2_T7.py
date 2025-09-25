print("Program starting.")

fahr = int(input("Insert fahrenheits: "))

cels = round((fahr - 32) / 1.8, 1)
print(f"{fahr}°F is {cels}°C")
print("Program ending.")