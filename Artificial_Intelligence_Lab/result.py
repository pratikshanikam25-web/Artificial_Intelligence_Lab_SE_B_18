subjects = ["Maths", "Physics", "Data Structures", "Python", "Digital Finance"]

print("Enter marks for the following subjects (out of 100):")

total = 0

# Take input for 5 subjects
for subject in subjects:
    marks = float(input("Enter marks in " + subject + ": "))
    total = total + marks

# Calculate percentage
percentage = total / 5

# Display result
print("\nTotal Marks =", total, "/ 500")
print("Percentage =", percentage, "%")

# Grade using if-else
if percentage < 40:
    print("Grade: Fail")
elif percentage < 65:
    print("Grade: II Class")
elif percentage < 75:
    print("Grade: I Class")
else:
    print("Grade: Distinction")
