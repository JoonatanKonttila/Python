DELIMITER = ";"
WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday")

class TIMESTAMP:
    def __init__(self):
        self.weekday = ""
        self.hour = ""
        self.consumption = 0.0
        self.price = 0.0

class DAY_USAGE:
    def __init__(self):
        self.weekday = ""
        self.total_consumption = 0.0
        self.total_cost = 0.0

def readFile(PFilename: str, PTimestamps: list) -> None:
    print(f'Reading file "{PFilename}".')
    PTimestamps.clear()
    try:
        with open(PFilename, "r") as f:
            f.readline()  # skip header
            for line in f:
                line = line.strip()
                if line:
                    cols = line.split(DELIMITER)
                    ts = TIMESTAMP()
                    ts.weekday = cols[0]
                    ts.hour = cols[1]
                    ts.consumption = float(cols[2])
                    ts.price = float(cols[3])
                    PTimestamps.append(ts)
    except FileNotFoundError:
        print(f'File "{PFilename}" not found!')
    return None

def analyseTimestamps(PTimestamps: list, PResults: list) -> None:
    print("Analysing timestamps.")
    PResults.clear()
    daily_usage: list[DAY_USAGE] = [DAY_USAGE() for _ in WEEKDAYS]

    for i, day in enumerate(WEEKDAYS):
        daily_usage[i].weekday = day
        for ts in PTimestamps:
            if ts.weekday == day:
                daily_usage[i].total_consumption += ts.consumption
                daily_usage[i].total_cost += ts.consumption * ts.price

    for du in daily_usage:
        PResults.append(f" - {du.weekday} usage {du.total_consumption:.2f} kWh, cost {du.total_cost:.2f} €")
    return None

def displayResults(PResults: list) -> None:
    print("Displaying results.")
    print("### Electricity consumption summary ###")
    for res in PResults:
        print(res)
    print("### Electricity consumption summary ###")
    return None

def main() -> None:
    print("Program starting.")
    PTimestamps: list[TIMESTAMP] = []
    Results: list[str] = []

    filename = input("Insert filename: ")
    readFile(filename, PTimestamps)
    analyseTimestamps(PTimestamps, Results)
    displayResults(Results)

    PTimestamps.clear()
    Results.clear()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
