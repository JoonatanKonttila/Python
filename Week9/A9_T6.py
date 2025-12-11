########################################################
# Task A9_T6
# Developer Aate Joonatan Konttila
# Date 2025-12-3
########################################################

def showOptions() -> None:
    print("Options:")
    print("1 - Insert line")
    print("2 - Save lines")
    print("0 - Exit")

def askChoice() -> str:
    return input("Your choice: ")

def insertLine(lines: list[str]) -> None:
    text = input("Insert text: ")
    lines.append(text)

def saveLines(lines: list[str]) -> None:
    if not lines:
        print("No lines to save.")
        return
    filename = input("Insert filename: ")
    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")
    print(f"Saved {len(lines)} lines to {filename}.")

def main() -> None:
    lines: list[str] = []
    print("Program starting.")
    try:
        while True:
            showOptions()
            choice = askChoice()
            if choice == "1":
                insertLine(lines)
            elif choice == "2":
                saveLines(lines)
            elif choice == "0":
                break
    except KeyboardInterrupt:
        print("\nKeyboard interrupt and unsaved progress!")
        if lines:
            save = input("Save before quit(y/n)?: ").strip().lower()
            if save == "y":
                saveLines(lines)
    print("Program ending.")

if __name__ == "__main__":
    main()
