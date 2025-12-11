########################################################
# Task A10_T2
# Developer Aate Joonatan Konttila
# Date 2025-12-4
########################################################

import sys

def readValues(PFilename: str, PValues: list[int]) -> None:
    try:
        with open(PFilename, "r") as f:
            for line in f:
                line = line.strip()
                if line != "":
                    try:
                        PValues.append(int(line))
                    except ValueError:
                        print(f'Error! Could not convert "{line}" to integer.')
                        sys.exit(1)
    except FileNotFoundError:
        print(f'File "{PFilename}" does not exist.')
        sys.exit(1)
    return None

def sumOfValues(PValues: list[int]) -> int:
    Sum = 0
    for val in PValues:
        Sum += val
    return Sum

def productOfValues(PValues: list[int]) -> int:
    Product = 1
    for val in PValues:
        Product *= val
    return Product

def main() -> None:
    Values: list[int] = []
    print("Program starting.")
    filename = input("Insert filename: ")
    readValues(filename, Values)
    total = sumOfValues(Values)
    prod = productOfValues(Values)
    print("# --- Sum of numbers --- #")
    print(total)
    print("# --- Sum of numbers --- #")
    print("# --- Product of numbers --- #")
    print(prod)
    print("# --- Product of numbers --- #")
    Values.clear()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
