WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday")

def readFile(PFilename: str, PRows: list[str]) -> None:
    print('Reading file "{}".'.format(PFilename))
    PRows.clear()
    try:
        with open(PFilename, "r") as f:
            header = f.readline()  # skip header
            for line in f:
                line = line.strip()
                if line:  # skip empty lines
                    PRows.append(line)
    except FileNotFoundError:
        print(f'File "{PFilename}" not found!')
    return None

def analyseTimestamps(PRows: list[str], PResults: list[str]) -> None:
    print("Analysing timestamps.")
    PResults.clear()
    WeekdayTimestampAmount = [0] * len(WEEKDAYS)
    for row in PRows:
        for i, day in enumerate(WEEKDAYS):
            if row.startswith(day):
                WeekdayTimestampAmount[i] += 1
                break
    for i, day in enumerate(WEEKDAYS):
        PResults.append(f" - {day} {WeekdayTimestampAmount[i]} stamps")
    return None

def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    print("### Timestamp analysis ###")
    for res in PResults:
        print(res)
    print("### Timestamp analysis ###")
    return None

def main() -> None:
    print("Program starting.")
    Rows: list[str] = []
    Results: list[str] = []
    
    filename = input("Insert filename: ")
    readFile(filename, Rows)
    analyseTimestamps(Rows, Results)
    displayResults(Results)
    
    Rows.clear()
    Results.clear()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
