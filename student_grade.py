
name = input("Enter a name:")

m1 = int(input("Enter a number:"))
m2 = int(input("Enter a number:"))
m3 = int(input("Enter a number:"))

total = m1 + m2 + m3
average = total / 3

if average >= 80:
    print("Grade A")
elif average >= 70:
    print("Grade B")
else:
    print("Grade C")

print("Student:", name)
print("Total:", total)
print("Average:", average)
