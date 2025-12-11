from calculator_lib import add, subtract, multiply, divide

def showOptions() -> None:
    print("Options:")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("0 - Exit")

def askChoice() -> int:
    choice = input("Your choice: ").strip()
    if choice.isdigit():
        return int(choice)
    return -1  # invalid choice

def askValue(PPrompt: str) -> float:
    while True:
        value_str = input(PPrompt).strip()
        try:
            return float(value_str)
        except ValueError:
            print("Invalid input! Enter a number.")

def main() -> None:
    print("Program starting.")
    while True:
        showOptions()
        choice = askChoice()
        print()
        if choice == 0:
            print("Exiting program.\n")
            break
        elif choice in (1, 2, 3, 4):
            val1 = askValue("Insert first value: ")
            val2 = askValue("Insert second value: ")
            if choice == 1:
                result = add(val1, val2)
                print(f"{val1} + {val2} = {result}\n")
            elif choice == 2:
                result = subtract(val1, val2)
                print(f"{val1} - {val2} = {result}\n")
            elif choice == 3:
                result = multiply(val1, val2)
                print(f"{val1} * {val2} = {result}\n")
            elif choice == 4:
                result = divide(val1, val2)
                if val2 != 0:
                    print(f"{val1} / {val2} = {result}\n")
        else:
            print("Unknown option! Try again.\n")
    print("Program ending.")

if __name__ == "__main__":
    main()
