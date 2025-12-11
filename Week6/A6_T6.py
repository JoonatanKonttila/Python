LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rot13_char(c):
    if c.islower():
        index = LOWER_ALPHABETS.index(c)
        return LOWER_ALPHABETS[(index + 13) % 26]
    elif c.isupper():
        index = UPPER_ALPHABETS.index(c)
        return UPPER_ALPHABETS[(index + 13) % 26]
    else:
        return c

def rot13_text(text):
    return "".join(rot13_char(c) for c in text)

def main():
    print("Program starting.\n")
    
    print("Collecting plain text rows for ciphering.")
    rows = []
    while True:
        row = input("Insert row(empty stops): ")
        if row == "":
            break
        rows.append(row)
    
    ciphered_rows = [rot13_text(row) for row in rows]
    
    print("\n#### Ciphered text ####")
    for row in ciphered_rows:
        print(row)
    
    print("\n#### Ciphered text ####")
    
    save_choice = input("\nDo you want to save the ciphered text to a file? (y/n): ").lower()
    if save_choice == "y":
        filename = input("Insert filename to save: ")
        with open(filename, "w") as f:
            for row in ciphered_rows:
                f.write(row + "\n")
        print("Ciphered text saved!")
    
    print("Program ending.")

if __name__ == "__main__":
    main()
