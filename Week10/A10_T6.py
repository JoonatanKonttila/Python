########################################################
# Task A10_T6
# Developer Aate Joonatan Konttila
# Date 2025-12-4
########################################################

import copy
import time
from typing import Callable

def readValues(PValues: list[int]) -> None:
    PValues.clear()
    filename = input("Insert dataset filename: ")
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if line != "":
                    PValues.append(int(line))
        print(f"Dataset '{filename}' read successfully.")
    except FileNotFoundError:
        print(f"File '{filename}' does not exist.")
    return None

def bubbleSort(PNums: list[int]) -> list[int]:
    n = len(PNums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if PNums[j] > PNums[j + 1]:
                PNums[j], PNums[j + 1] = PNums[j + 1], PNums[j]
    return PNums

def quickSort(PNums: list[int]) -> list[int]:
    if len(PNums) <= 1:
        return PNums
    pivot = PNums[0]
    left = [x for x in PNums[1:] if x <= pivot]
    right = [x for x in PNums[1:] if x > pivot]
    return quickSort(left) + [pivot] + quickSort(right)

def measureSortingTime(PSortingAlgorithm: Callable, PArr: list[int]) -> int:
    StartTime = time.perf_counter_ns()
    if PSortingAlgorithm == sorted:
        PSortingAlgorithm(PArr)
    else:
        PSortingAlgorithm(PArr)
    EndTime = time.perf_counter_ns()
    return EndTime - StartTime

def saveResults(Results: list[str]) -> None:
    if len(Results) == 0:
        print("No results to save.")
        return
    filename = input("Insert results filename: ")
    try:
        with open(filename, "w") as f:
            for line in Results:
                f.write(line + "\n")
        print(f"Results saved to '{filename}'")
    except Exception as e:
        print(f"Error saving results: {e}")
    return None

def main() -> None:
    Values: list[int] = []
    Results: list[str] = []
    print("Program starting.")

    while True:
        print("\nOptions:")
        print("1 - Read dataset values")
        print("2 - Measure speeds")
        print("3 - Save results")
        print("0 - Exit")
        choice = input("Your choice: ").strip()

        if choice == "1":
            readValues(Values)
        elif choice == "2":
            if len(Values) == 0:
                print("No dataset loaded. Please read dataset first.")
                continue
            dataset_name = input("Enter dataset name for display: ").strip()
            BuiltinSortedTimeNs = measureSortingTime(sorted, copy.deepcopy(Values))
            BubbleSortTimeNs = measureSortingTime(bubbleSort, copy.deepcopy(Values))
            QuickSortTimeNs = measureSortingTime(quickSort, copy.deepcopy(Values))
            print(f"Measured speeds for dataset '{dataset_name}':")
            print(f" - Built-in sorted {BuiltinSortedTimeNs} ns")
            print(f" - Buble sort {BubbleSortTimeNs} ns")
            print(f" - Quick sort {QuickSortTimeNs} ns")
            Results.append(f"Measured speeds for dataset '{dataset_name}':")
            Results.append(f" - Built-in sorted {BuiltinSortedTimeNs} ns")
            Results.append(f" - Buble sort {BubbleSortTimeNs} ns")
            Results.append(f" - Quick sort {QuickSortTimeNs} ns")
        elif choice == "3":
            saveResults(Results)
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, try again.")

    Values.clear()
    Results.clear()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
