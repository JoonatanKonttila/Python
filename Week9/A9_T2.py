########################################################
# Task A9_T2
# Developer Aate Joonatan Konttila
# Date 2025-12-3
########################################################

import sys

def main() -> None:
    print("Program starting.")
    code_str = input("Insert exit code(0-255): ")
    try:
        code = int(code_str)
    except ValueError:
        code = 1
    if code < 0 or code > 255:
        code = 1
    print("Clean exit")
    sys.exit(code)

if __name__ == "__main__":
    main()
