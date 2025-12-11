def showOptions():
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit count")
    return None

def askChoice():
    choice = input("Your choice: ")
    return choice

def main():
    print("Program starting.")
    count = 0
    choice = -1

    while choice != 0:
        showOptions()
        strChoice = askChoice()
        
        if strChoice.isnumeric():
            choice = (int(strChoice))
        else:
            print("Unknown option! Try again.\n")
            continue

        match choice:
            case 1:
                print(f"Current count - {count}\n")
            case 2:
                count += 1
                print("Count increased!\n")
            case 3:
                count = 0
                print("Cleared count!\n")
            case 0:
                print("Exiting program.\n")
                break
            case _:
                print("Unknown option! Try again.\n")
    print("Program ending.")
    return None



if __name__ == "__main__":
    main()