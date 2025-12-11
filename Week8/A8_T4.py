from datetime import datetime

MONTHS = (
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
)

WEEKDAYS = (
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
)

def readTimestamps(PFilename: str, PTimestamps: list[datetime]) -> None:
    PTimestamps.clear()
    try:
        with open(PFilename, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        ts = datetime.strptime(line, "%Y-%m-%d %H:%M")
                        PTimestamps.append(ts)
                    except ValueError:
                        print(f"Invalid timestamp skipped: {line}")
    except FileNotFoundError:
        print(f"File not found: {PFilename}")

def calculateYears(PYear: int, PTimestamps: list[datetime]) -> int:
    count = 0
    for ts in PTimestamps:
        if ts.year == PYear:
            count += 1
    return count

def calculateMonths(PMonth: str, PTimestamps: list[datetime]) -> int:
    count = 0
    if PMonth not in MONTHS:
        return 0
    month_index = MONTHS.index(PMonth) + 1
    for ts in PTimestamps:
        if ts.month == month_index:
            count += 1
    return count

def calculateWeekdays(PWeekday: str, PTimestamps: list[datetime]) -> int:
    count = 0
    if PWeekday not in WEEKDAYS:
        return 0
    weekday_index = WEEKDAYS.index(PWeekday)
    for ts in PTimestamps:
        if ts.weekday() == weekday_index:
            count += 1
    return count

def showOptions() -> None:
    print("Options:")
    print("1 - Calculate amount of timestamps during year")
    print("2 - Calculate amount of timestamps during month")
    print("3 - Calculate amount of timestamps during weekday")
    print("0 - Exit")

def askChoice() -> int:
    choice = input("Your choice: ").strip()
    if choice.isdigit():
        return int(choice)
    return -1

def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ").strip()
    timestamps: list[datetime] = []
    readTimestamps(filename, timestamps)
    print()
    while True:
        showOptions()
        choice = askChoice()
        print()
        if choice == 0:
            print("Exiting program.\n")
            break
        elif choice == 1:
            year_str = input("Insert year: ").strip()
            if year_str.isdigit():
                year = int(year_str)
                count = calculateYears(year, timestamps)
                print(f"Amount of timestamps during year '{year}' is {count}\n")
            else:
                print("Invalid year input.\n")
        elif choice == 2:
            month = input("Insert month: ").strip()
            count = calculateMonths(month, timestamps)
            print(f"Amount of timestamps during month '{month}' is {count}\n")
        elif choice == 3:
            weekday = input("Insert weekday: ").strip()
            count = calculateWeekdays(weekday, timestamps)
            print(f"Amount of timestamps during weekday '{weekday}' is {count}\n")
        else:
            print("Unknown option! Try again.\n")
    print("Program ending.")

if __name__ == "__main__":
    main()
