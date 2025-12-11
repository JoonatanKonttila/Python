import os

# rot13
def rot13(text):
    """Encipher or decipher text using ROT13."""
    LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
    UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    result = ""
    for c in text:
        if c.islower():
            index = LOWER_ALPHABETS.index(c)
            result += LOWER_ALPHABETS[(index + 13) % 26]
        elif c.isupper():
            index = UPPER_ALPHABETS.index(c)
            result += UPPER_ALPHABETS[(index + 13) % 26]
        else:
            result += c
    return result

# Locations map
locations = ["home", "Galba's palace", "Otho's palace", "Vitellius' palace", "Vespasian's palace"]

def initialize_progress_file():
    """Create player_progress.txt if it does not exist."""
    if not os.path.exists("player_progress.txt"):
        with open("player_progress.txt", "w") as f:
            f.write("current_location;next_location;passphrase\n")
            # Initialize with starting point home
            f.write("0;1;qvfpvcyvar\n")

def read_progress():
    """Read the last progress row from player_progress.txt."""
    with open("player_progress.txt", "r") as f:
        lines = f.readlines()
        if len(lines) <= 1:
            # No progress, return first row
            return ("0", "1", "qvfpvcyvar")
        else:
            last_line = lines[-1].strip()
            return tuple(last_line.split(";"))

def append_progress(current, next_loc, passphrase):
    """Append a new progress row to player_progress.txt."""
    with open("player_progress.txt", "a") as f:
        f.write(f"{current};{next_loc};{passphrase}\n")

def travel_to_next_location():
    print("Travel starting.")
    
    current, next_loc, passphrase_rot = read_progress()
    current = int(current)
    next_loc = int(next_loc)
    passphrase_plain = rot13(passphrase_rot)

    print(f"Currently at {locations[current]}.")
    print(f"Travelling to {locations[next_loc]}...")
    print(f"...Arriving to the {locations[next_loc]}.")
    print("Passing the guard at the entrance.")
    print(f'"{passphrase_plain}"')
    
    # Simulate message file
    gkg_filename = f"{next_loc}_{passphrase_rot}.gkg"
    if not os.path.exists(gkg_filename):
        # test
        message = f"Cneg {next_loc} - Lrne bs gur Sbhe Rzcrebef:\nVa NQ 68, nsgre Areb'f qrngu, Ebzr cyhatrq vagb punbf."
        with open(gkg_filename, "w") as f:
            f.write(message)
    
    print("Looking for the message in the palace...")
    print("Ah, there it is! Seems cryptic.")
    
    # Read the ciphered message
    with open(gkg_filename, "r") as f:
        ciphered_message = f.readline().strip()
    
    append_progress(next_loc, "-", ciphered_message)

    # Decipher the message and save to plain text file
    plain_message = rot13(ciphered_message)
    plain_filename = f"{next_loc}-{passphrase_plain}.txt"
    with open(plain_filename, "w") as f:
        f.write(plain_message + "\n")
    
    print("[Game] Progress autosaved!")
    print("Deciphering Emperor's message...")
    print("Looks like I've got now the plain version copy of the Emperor's message.")
    print("Time to leave...")
    print("Travel ending.")

if __name__ == "__main__":
    initialize_progress_file()
    travel_to_next_location()
