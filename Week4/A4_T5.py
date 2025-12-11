print("Program starting.\n")

startNum = int(input("Insert starting point: "))
stoptNum = int(input("Insert stopping point: "))
inspNum = int(input("Insert inspection point: "))

keepGoing = True

if startNum > stoptNum:
    keepGoing = False
    print("\nStarting point value must be less than the stopping point value.")
elif inspNum < startNum or inspNum > stoptNum:
    keepGoing = False
    print("\nInspection value must be within the range of the start and stop.")
else:
    keepGoing = True


if keepGoing == True:
    print("\nFirst loop - inspection with break:")
    first_output = []
    for i in range(startNum, stoptNum):
        if i == inspNum:
            break
        first_output.append(str(i))
    print(" ".join(first_output))

    print("Second loop - inspection with continue:")
    second_output = []

    for i in range(startNum, stoptNum):
        if i == inspNum:
            continue
        second_output.append(str(i))

    print(" ".join(second_output))


print("\nProgram ending.")
