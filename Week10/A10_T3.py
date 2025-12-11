########################################################
# Task A10_T1
# Developer Aate Joonatan Konttila
# Date 2025-12-4
########################################################

import sys

def readValues(PFilename: str, PValues: list[int]) -> None:
    try:
        with open(PFilename, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    PValues.append(int(line))
    except Exception as e:
        print(f"Error reading file '{PFilename}': {e}")
        sys.exit(1)
    return None

def bubbleSort(PValues: list[int], PAsc: bool = True) -> None:
    n = len(PValues)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if (PAsc and PValues[j] > PValues[j + 1]) or (not PAsc and PValues[j] < PValues[j + 1]):
                PValues[j], PValues[j + 1] = PValues[j + 1], PValues[j]
    return None

def main() -> None:
    print("Program starting.")

    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = input("Insert filename: ")

    values: list[int] = []
    readValues(filename, values)

    print(f"Raw '{filename}' -> {', '.join(str(v) for v in values)}")

    bubbleSort(values, True)
    print(f"Ascending '{filename}' -> {', '.join(str(v) for v in values)}")

    bubbleSort(values, False)
    print(f"Descending '{filename}' -> {', '.join(str(v) for v in values)}")

    print("Program ending.")
    values.clear()
    return None

if __name__ == "__main__":
    main()
