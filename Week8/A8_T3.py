def showOptions() -> None:
    print("Options:")
    print("1 - Read values")
    print("2 - Amount of values")
    print("3 - Calculate sum of values")
    print("4 - Calculate average of values")
    print("0 - Exit")

def askChoice() -> int:
    choice = input("Your choice: ").strip()
    if choice.isdigit():
        return int(choice)
    return -1

def readValues(filename: str) -> list[float]:
    values: list[float] = []
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if line:  # skip empty lines
                    try:
                        values.append(float(line))
                    except ValueError:
                        print(f"Invalid number ignored: {line}")
    except FileNotFoundError:
        print(f"File not found: {filename}")
    return values

def calculateSum(values: list[float]) -> float:
    return round(sum(values), 1)

def calculateAverage(values: list[float]) -> float:
    if values:
        return round(sum(values) / len(values), 1)
    return 0.0

def main() -> None:
    print("Program starting.")
    values: list[float] = []

    while True:
        showOptions()
        choice = askChoice()
        print()
        if choice == 0:
            print("Exiting program.\n")
            break
        elif choice == 1:
            filename = input("Insert filename: ").strip()
            values = readValues(filename)
            print()
        elif choice == 2:
            print(f"Amount of values {len(values)}\n")
        elif choice == 3:
            total = calculateSum(values)
            print(f"Sum of values {total}\n")
        elif choice == 4:
            avg = calculateAverage(values)
            print(f"Average of values {avg}\n")
        else:
            print("Unknown option! Try again.\n")

    print("Program ending.")

if __name__ == "__main__":
    main()
