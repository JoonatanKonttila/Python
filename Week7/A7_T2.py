def main():
    print("Program starting.\n")
    
    user_input = input("Insert comma separated integers: ")
    
    # Split input by commas
    entries = user_input.split(",")
    
    valid_integers = []
    
    for entry in entries:
        entry = entry.strip()
        if entry == "":
            continue
        try:
            number = int(entry)
            valid_integers.append(number)
        except ValueError:
            print(f"Invalid value detected: '{entry}'")
    
    if not valid_integers:
        print("No valid integers to analyze.")
    else:
        total_count = len(valid_integers)
        total_sum = sum(valid_integers)
        parity = "even" if total_sum % 2 == 0 else "odd"
        
        print(f"There are {total_count} integers in the list.")
        print(f"Sum of the integers is {total_sum} and it's {parity}")
    
    print("\nProgram ending.")

if __name__ == "__main__":
    main()
