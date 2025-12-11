########################################################
# Task A9_T5
# Developer Aate Joonatan Konttila
# Date 2025-12-3
########################################################

def collectByte(color_name: str) -> int:
    feed = input(f"Insert {color_name}: ")
    value = int(feed)
    if not 0 <= value <= 255:
        raise ValueError("Out of range")
    return value

def main() -> None:
    print("Program starting.")
    try:
        r = collectByte("red")
        g = collectByte("green")
        b = collectByte("blue")
        print("RGB Details:")
        print(f"- Red {r}")
        print(f"- Green {g}")
        print(f"- Blue {b}")
        print(f"- Hex #{r:02x}{g:02x}{b:02x}")
    except Exception:
        print("Couldn't perform the designed task due to the invalid input values.")
    print("Program ending.")

if __name__ == "__main__":
    main()
