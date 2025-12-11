SEPARATOR = ";"

def readValues() -> str:
    filename = input("Insert filename: ")
    values_str = ""
    try:
        with open(filename, "r") as f:
            for line in f:
                number = line.strip()
                if number:
                    values_str += number + SEPARATOR
        values_str = values_str.rstrip(SEPARATOR)
    except FileNotFoundError:
        print(f'File "{filename}" not found!')
        return ""
    return values_str

def analyseNumbers(values_str: str) -> str:
    if not values_str:
        return ""
    
    numbers = [int(n) for n in values_str.split(SEPARATOR)]
    count = len(numbers)
    total = sum(numbers)
    greatest = max(numbers)
    average = total / count if count > 0 else 0
    average_formatted = "{:.2f}".format(average)
    
    return f"{count}{SEPARATOR}{total}{SEPARATOR}{greatest}{SEPARATOR}{average_formatted}"

def main():
    print("Program starting.")
    
    values_str = readValues()
    if not values_str:
        print("Program ending.")
        return
    
    analysis_result = analyseNumbers(values_str)
    
    print("#### Number analysis - START ####")
    print(f'File "A6_T5_D1.txt" results:')
    print("Count;Sum;Greatest;Average")
    print(analysis_result)
    print("\n#### Number analysis - END ####")
    
    print("Program ending.")

if __name__ == "__main__":
    main()
