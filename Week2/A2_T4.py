print("Program starting.")
print("Estimate how many minutes you spent on programming...\n")

T1= int(input("A1_T1: "))
T2= int(input("A1_T2: "))
T3= int(input("A1_T3: "))
T4= int(input("A1_T4: "))
T5= int(input("A1_T5: "))
T6= int(input("A1_T6: "))
T7= int(input("A1_T7: "))

total = int(T1+T2+T3+T4+T5+T6+T7)
avg = round(float(total/7), 2)
rounded = round(avg)

print(f"In total you spent {total} minutes on programming.")
print(f"Average per task was {avg} min and same rounded to the nearest integer {rounded} min.\n")
print("Program ending.")