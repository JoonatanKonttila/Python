choice = -1
word = ""

while choice != 0:
    print("Options:")
    print("1 - Insert word")
    print("2 - Show current word")
    print("3 - Show current word in reverse")
    print("0 - Exit")
    choice = int(input("Your choice: "))
    match choice:
        case 1:
            word = input("Insert word: ")
            print()
        case 2:
            print(f'Current word "{word}"\n')
        case 3:
            print(f"Word reversed - {word[::-1]}\n")
        case 0:
            print("Exiting program.\n")
            break
        case _:
            print("Unknown option! Try again.\n")
        
print("Program ending.")