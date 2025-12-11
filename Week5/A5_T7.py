DELIMITER = ","

def collectWords():
    words = []
    while True:
        word = input("Insert word(empty stops): ")
        if word == "":
            break
        words.append(word)
    return DELIMITER.join(words)

def analyseWords(words_str):
    words_list = words_str.split(DELIMITER) if words_str else []

    num_words = len(words_list)
    chars = sum(len(word) for word in words_list)
    avg = chars / num_words if num_words > 0 else 0

    print(f"- {num_words} words")
    print(f"- {chars} characters")
    print("- {:.2f} average word length".format(avg))
    

def main():
    print("Program starting.")
    words = collectWords()
    analyseWords(words)
    print("Program ending.")

if __name__ == "__main__":
    main()