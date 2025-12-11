########################################################
# Task A10_T1
# Developer Aate Joonatan Konttila
# Date 2025-12-4
########################################################

def readFile(filename: str) -> list[str]:
    values = []
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if line != "":
                    values.append(line)
    except FileNotFoundError:
        print(f'File "{filename}" does not exist.')
    return values

def displayVertical(values: list[str]) -> None:
    print("# --- Vertically --- #")
    for val in values:
        print(val)
    print("# --- Vertically --- #")

def displayHorizontal(values: list[str]) -> None:
    print("# --- Horizontally --- #")
    print(", ".join(values))
    print("# --- Horizontally --- #")

def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ")
    values = readFile(filename)
    if values:
        displayVertical(values)
        displayHorizontal(values)
    print("Program ending.")

if __name__ == "__main__":
    main()
