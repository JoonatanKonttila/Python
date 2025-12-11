########################################################
# Task A10_T7
# Developer Aate Joonatan Konttila
# Date 2025-12-4
########################################################

import random

random.seed(1234)

def layMines(PMineField: list[list[int]], PMines: int) -> None:
    """Randomly places PMines mines (value 9) into the pre-initialized PMineField."""
    Rows = len(PMineField)
    Cols = len(PMineField[0]) if Rows > 0 else 0
    placed = 0
    while placed < PMines:
        r = random.randint(0, Rows - 1)
        c = random.randint(0, Cols - 1)
        if PMineField[r][c] != 9:
            PMineField[r][c] = 9
            placed += 1

def calculateNearbys(PMineField: list[list[int]]) -> None:
    """Calculates the number of nearby mines for each non-mine cell."""
    Rows = len(PMineField)
    Cols = len(PMineField[0]) if Rows > 0 else 0
    for r in range(Rows):
        for c in range(Cols):
            if PMineField[r][c] == 9:
                continue
            count = 0
            # Check all 8 surrounding cells
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < Rows and 0 <= nc < Cols:
                        if PMineField[nr][nc] == 9:
                            count += 1
            PMineField[r][c] = count

def generateMinefield(
        PMineField: list[list[int]],
        PRows: int,
        PCols: int,
        PMines: int) -> None:
    """Generates the minefield with given rows, columns, and number of mines."""
    PMineField.clear()
    for _ in range(PRows):
        PMineField.append([0] * PCols)
    layMines(PMineField, PMines)
    calculateNearbys(PMineField)

def showBoard(PMineField: list[list[int]]) -> None:
    """Prints the minefield to the console."""
    for row in PMineField:
        print(row)

def saveBoard(PMineField: list[list[int]], filename: str) -> None:
    """Saves the minefield to a CSV file."""
    with open(filename, "w") as f:
        for row in PMineField:
            line = ",".join(str(cell) for cell in row) + "\n"
            f.write(line)
    print(f"Board saved into '{filename}'")

def main() -> None:
    MineField: list[list[int]] = []
    print("Program starting.")

    while True:
        print("Options:")
        print("1 - Generate minesweeper board")
        print("2 - Show generated board")
        print("3 - Save generated board")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            try:
                rows = int(input("Insert rows: "))
                cols = int(input("Insert columns: "))
                mines = int(input("Insert mines: "))
                if mines > rows * cols:
                    print("Error: Too many mines for the given board size.")
                    continue
                generateMinefield(MineField, rows, cols, mines)
            except ValueError:
                print("Invalid input! Must be integers.")
        elif choice == "2":
            if not MineField:
                print("No board generated yet.")
            else:
                showBoard(MineField)
        elif choice == "3":
            if not MineField:
                print("No board generated yet.")
            else:
                filename = input("Insert filename: ")
                saveBoard(MineField, filename)
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

    print("Program ending.")

if __name__ == "__main__":
    main()
