########################################################
# Task A9_T4
# Developer Aate Joonatan Konttila
# Date 2025-12-3
########################################################

TEMP_MIN = -273.15
TEMP_MAX = 10000

def collectCelsius() -> float:
    feed = input("Insert Celsius: ")
    try:
        celsius = float(feed)
    except ValueError:
        raise ValueError(f"could not convert string to float: '{feed}'")
    if not TEMP_MIN <= celsius <= TEMP_MAX:
        raise Exception(f"{celsius} temperature out of range.")
    return celsius

def main() -> None:
    print("Program starting.")
    try:
        value = collectCelsius()
        print(f"You inserted {value} °C")
    except Exception as e:
        print(f"Error! {e}")
    print("Program ending.")

if __name__ == "__main__":
    main()
