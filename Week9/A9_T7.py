########################################################
# Task A9_T7
# Developer Aate Joonatan Konttila
# Date 2025-12-3
########################################################

import sys
import os

def showHelp() -> None:
    print("Usage: python A9_T7.py <source_file> <destination_file>")

def copyFile(srcFile: str, dstFile: str) -> None:
    proceed = True
    if os.path.exists(dstFile):
        answer = input(f'Destination file "{dstFile}" exists. Overwrite? (y/n): ').strip().lower()
        if answer != "y":
            print("Copy cancelled by user.")
            proceed = False
    if proceed:
        try:
            with open(srcFile, "r", encoding="utf-8") as f:
                content = f.read()
            with open(dstFile, "w", encoding="utf-8") as f:
                f.write(content)
            print(f'Copying file "{srcFile}" to "{dstFile}".')
        except Exception as e:
            print(f"Error occurred during copying: {e}")
            sys.exit(-1)

def main() -> None:
    print("Program starting.")
    if len(sys.argv) != 3:
        print("Invalid amount of arguments.")
        showHelp()
        print("Program ending.")
        return
    srcFile = sys.argv[1]
    dstFile = sys.argv[2]
    if not os.path.exists(srcFile):
        print(f'Source file "{srcFile}" does not exist.')
        sys.exit(-1)
    print(f'Source file "{srcFile}"')
    print(f'Destination file "{dstFile}"')
    copyFile(srcFile, dstFile)
    print("Program ending.")

if __name__ == "__main__":
    main()
