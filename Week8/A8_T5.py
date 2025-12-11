import hashlib
import os

CREDENTIALS_FILE = "credentials.txt"
DELIMITER = ";"

def hash_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()

def load_credentials() -> list[tuple[int, str, str]]:
    credentials = []
    if not os.path.exists(CREDENTIALS_FILE):
        return credentials
    with open(CREDENTIALS_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                parts = line.split(DELIMITER)
                if len(parts) == 3:
                    credentials.append((int(parts[0]), parts[1], parts[2]))
    return credentials

def save_credentials(credentials: list[tuple[int, str, str]]) -> None:
    with open(CREDENTIALS_FILE, "w") as f:
        for entry in credentials:
            f.write(f"{entry[0]}{DELIMITER}{entry[1]}{DELIMITER}{entry[2]}\n")

def register_user() -> None:
    username = input("Insert username: ").strip()
    password = input("Insert password: ").strip()
    hashed = hash_password(password)
    credentials = load_credentials()
    user_id = len(credentials)
    credentials.append((user_id, username, hashed))
    save_credentials(credentials)
    print("User registration completed!\n")

def login_user() -> None:
    username = input("Insert username: ").strip()
    password = input("Insert password: ").strip()
    hashed = hash_password(password)
    credentials = load_credentials()
    for user in credentials:
        if user[1] == username and user[2] == hashed:
            print(f"Login successful. Welcome {username}!\n")
            user_menu(username)
            return
    print("Login failed. Invalid username or password.\n")

def user_menu(username: str) -> None:
    while True:
        print("User menu options:")
        print("1 - View profile")
        print("2 - Change password (not implemented)")
        print("0 - Logout")
        choice = input("Your choice: ").strip()
        if choice == "0":
            print(f"Logging out {username}.\n")
            break
        elif choice == "1":
            print(f"User profile: {username}\n")
        elif choice == "2":
            print("Change password is not implemented.\n")
        else:
            print("Unknown option! Try again.\n")

def show_main_menu() -> None:
    print("Options:")
    print("1 - Login")
    print("2 - Register")
    print("0 - Exit")

def main() -> None:
    print("Program starting.\n")
    while True:
        show_main_menu()
        choice = input("Your choice: ").strip()
        print()
        if choice == "0":
            print("Exiting program.\n")
            break
        elif choice == "1":
            login_user()
        elif choice == "2":
            register_user()
        else:
            print("Unknown option! Try again.\n")
    print("Program ending.")

if __name__ == "__main__":
    main()
