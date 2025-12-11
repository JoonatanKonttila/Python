def frameWord(PWord):
    frame = len(PWord) + 4
    print("*" * frame)
    print("* ", PWord, " *")
    print("*" * frame)
    return None

def main():
    print("Program starting.")
    sana = input("Insert word: ")
    print()

    frameWord(sana)

    print()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()