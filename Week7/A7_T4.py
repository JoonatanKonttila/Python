DELIMITER = ";"

class TIMESTAMP:
    def __init__(self):
        self.weekday = ""
        self.hour = ""
        self.consumption = 0.0
        self.price = 0.0

def readFile(PFilename: str, PTimestamps: list) -> None:
    print(f'Reading file "{PFilename}".')
    PTimestamps.clear()
    try:
        with open(PFilename, "r") as f:
            f.readline()  # skip header
            for line in f:
                line = line.strip()
                if line:
                    columns = line.split(DELIMITER)
                    ts = TIMESTAMP()
                    ts.weekday = columns[0]
                    ts.hour = columns[1]
                    ts.consumption = float(columns[2])
                    ts.price = float(columns[3])
                    PTimestamps.append(ts)
    except FileNotFoundError:
        print(f'File "{PFilename}" not found!')
    return None

def displayTimestamps(PTimestamps: list) -> None:
    print("Electricity usage:")
    for ts in PTimestamps:
        total_cost = ts.consumption * ts.price
        print(f" - {ts.weekday} {ts.hour}, price {ts.price:.2f}, consumption {ts.consumption:.2f} kWh, total {total_cost:.2f} €")
    return None

def main() -> None:
    print("Program starting.")
    PTimestamps: list[TIMESTAMP] = []

    filename = input("Insert filename: ")
    readFile(filename, PTimestamps)
    displayTimestamps(PTimestamps)

    PTimestamps.clear()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
