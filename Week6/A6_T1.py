print("Program starting.")
print("This program can read a file.")

filename = input("Insert filename: ")

print(f'#### Start "{filename}" ####')
f = open(filename)
print(f.read())
print(f'#### End "{filename}" ####')
print("Program ending.")