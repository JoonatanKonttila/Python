print("Program starting.\n")

words = list()

i = "1"
while True:
    i = input("Insert word (empty stops): ")

    if i == "":
        break

    words.append(i)

chars = sum(len(word) for word in words)

print("\nYou inserted:")
print(f"- ",len(words), "words")
print(f"- ",chars, "characters")

print("\nProgram ending.")