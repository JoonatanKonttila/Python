########################################################
# Task A10_T5
# Developer Aate Joonatan Konttila
# Date 2025-12-4
########################################################

import sys

def recursiveFactorial(PNum: int) -> int:
    if PNum <= 1:
        return 1
    return PNum * recursiveFactorial(PNum - 1)

def main() -> None:
    print("Program starting.")
    
    try:
        num = int(input("Insert factorial: "))
        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            result = recursiveFactorial(num)
            print(f"Factorial {num}!\n{num} = {result}")
    except ValueError as e:
        print(f"Invalid input: {e}")

    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
