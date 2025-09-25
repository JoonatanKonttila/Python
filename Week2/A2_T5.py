print("Program starting.\n")

wordd = input("Insert a closed compund word: ")
length = len(wordd)
#firstChar = wordd[0]
lastChar = wordd[-1]
reversed = wordd[::-1]

print(f"The word you inserted is '{wordd}' and in reverse it is '{reversed}'.")
print(f"The inserted word length is {length}")
#print(f"first character is '{firstChar}'")
print(f"Last character is '{lastChar}'\n")

print("Take substring from the inserted word by inserting...")
start = int(input("1) Starting point: "))
ending = int(input("2) Ending point: "))
step = int(input("3) Step size: "))

subSTR = wordd[start:ending:step]

print(f"\nThe word '{wordd}' sliced to the defined substring is '{subSTR}'.")
print("Program ending.")
