import sys
import os

def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ")
    if not os.path.isfile(filename):
        print(f"Error! File '{filename}' does not exist.")
        sys.exit(1)
    print(f"## {filename} ##")
    with open(filename, "r") as file:
        for line in file:
            print(line.rstrip())
    print(f"## {filename} ##")
    print("Program ending.")

if __name__ == "__main__":
    main()
