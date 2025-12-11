def main():
    print("Program starting.\n")
    print("Collect positive integers.")

    integers = []

    while True:
        try:
            user_input = int(input("Insert positive integer(negative stops): "))
        except ValueError:
            print("Invalid input! Please enter an integer.")
            continue

        if user_input < 0:
            break
        integers.append(user_input)

    print("Stopped collecting positive integers.\n")

    if not integers:
        print("No integers to display.")
    else:
        print(f"Displaying {len(integers)} integers:")
        for index, value in enumerate(integers):
            ordinal = index + 1
            print(f"- Index {index} => Ordinal {ordinal} => Integer {value}")

    print("\nProgram ending.")

if __name__ == "__main__":
    main()
