import time

def show_menu():
    print("Options:")
    print("1 - Set pause duration")
    print("2 - Activate pause")
    print("0 - Exit")

def ask_choice():
    choice = input("Your choice: ").strip()
    return choice

def set_pause_duration():
    while True:
        duration_str = input("Insert pause duration (s): ").strip()
        try:
            duration = float(duration_str)
            if duration < 0:
                print("Duration must be non-negative.")
                continue
            return duration
        except ValueError:
            print("Invalid input. Enter a number.")

def activate_pause(duration):
    print(f"Pausing for {duration} seconds.")
    time.sleep(duration)
    print("Unpaused.\n")

def main():
    print("Program starting.")
    pause_duration = 1.0  # default pause duration
    while True:
        show_menu()
        choice = ask_choice()
        print()
        if choice == "1":
            pause_duration = set_pause_duration()
            print()
        elif choice == "2":
            activate_pause(pause_duration)
        elif choice == "0":
            print("Exiting program.\n")
            break
        else:
            print("Unknown option! Try again.\n")
    print("Program ending.")

if __name__ == "__main__":
    main()
