print("Program starting.")

print("This is a program with a simple menu, where you can choose which operation the program performs.")
name = input("Before the menu please insert your name: ")

print("\nOptions:")
print("1 - Print welcome message")
print("2 - Print the name backwards")
print("3 - Print the first character")
print("4 - Show the amount of characters in the name")
print("0 - Exit")
choice = int(input("Your choice: "))

if choice == 1:
    print(f"Welcome {name}!")
elif choice == 2:
    print(f'your name backwards is "{name[::-1]}"')
elif choice == 3:
    print(f'The first character in the name "{name}" is "{name[0]}"')
elif choice == 4:
    print(f'There are {len(name)} characters in the name "{name}"')
elif choice == 0:
    print("Exiting...")
else:
    print("Unknown option.")

print()
print("Program ending.")