print("Program starting.")
print("This program analyses a list of names from a file.")

filename = input("Insert filename to read: ")

print(f'Reading names from "{filename}".')

names_str = ""
names_list = []

try:
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                names_list.append(line)
    
    names_str = ";".join(names_list)
    
except FileNotFoundError:
    print(f'File "{filename}" not found!')
    print("Program ending.")
    exit()

print("Analysing names...")

name_count = len(names_list)
shortest_length = min(len(name) for name in names_list) if names_list else 0
longest_length = max(len(name) for name in names_list) if names_list else 0
average_length = (sum(len(name) for name in names_list) / name_count) if name_count > 0 else 0

print("Analysis complete!")

print("#### REPORT BEGIN ####")
print(f"Name count - {name_count}")
print(f"Shortest name - {shortest_length} chars")
print(f"Longest name - {longest_length} chars")
print("- Average name - {:.2f} chars".format(average_length))
print("#### REPORT END ####")
print("Program ending.")
