print("Program starting.")
name = input("What is your name: ")
num1txt = input("Enter a floating point number: ")
num1 = float(num1txt)
num2txt = input("Enter second floating point number: ")
num2 = float(num2txt)

print(f"{name} you gave numbers {num1} and {num2}")
#Kerrotaan ja pyöristetään.
multipliedNum = round(num1*num2, 2)
print(f"Multiplying first and second number will result in product {multipliedNum}")
print("Program ending.")