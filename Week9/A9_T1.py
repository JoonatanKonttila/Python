########################################################
# Task A9_T1
# Developer Aate Joonatan Konttila
# Date 2025-12-3
########################################################

def main() -> None:
    print("Program starting.\n")
    total: float = 0.0
    while True:
        value_str = input("Insert a floating-point value (0 to stop): ")
        try:
            value = float(value_str)
        except ValueError:
            print(f"Error! '{value_str}' couldn't be converted to float.")
            continue
        if value == 0:
            break
        total += value
    print(f"\nFinal sum is {total:.2f}")
    print("Program ending.")

if __name__ == "__main__":
    main()
