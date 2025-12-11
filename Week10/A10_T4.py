########################################################
# Task A10_T4
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

def merge(PLeft: list[int], PRight: list[int], PMerge: list[int], PAsc: bool = True) -> None:
    i = j = 0
    PMerge.clear()
    while i < len(PLeft) and j < len(PRight):
        if (PAsc and PLeft[i] <= PRight[j]) or (not PAsc and PLeft[i] >= PRight[j]):
            PMerge.append(PLeft[i])
            i += 1
        else:
            PMerge.append(PRight[j])
            j += 1
    while i < len(PLeft):
        PMerge.append(PLeft[i])
        i += 1
    while j < len(PRight):
        PMerge.append(PRight[j])
        j += 1
    return None

def mergeSort(PValues: list[int], PAsc: bool = True) -> None:
    if len(PValues) <= 1:
        return
    mid = len(PValues) // 2
    left = PValues[:mid]
    right = PValues[mid:]
    mergeSort(left, PAsc)
    mergeSort(right, PAsc)
    merge(left, right, PValues, PAsc)
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

    mergeSort(values, True)
    print(f"Ascending '{filename}' -> {', '.join(str(v) for v in values)}")

    mergeSort(values, False)
    print(f"Descending '{filename}' -> {', '.join(str(v) for v in values)}")

    print("Program ending.")
    values.clear()
    return None

if __name__ == "__main__":
    main()
