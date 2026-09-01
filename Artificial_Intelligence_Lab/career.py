subjects = ["Maths", "Physics", "Programming", "Biology",
            "Chemistry", "Circuits", "Statistics", "AI Concepts"]

print("Subjects List:")
for subject in subjects:
    print(subject)

first = input("Enter first subject you like: ").lower()
second = input("Enter second subject you like: ").lower()

if (first == "maths" and second == "physics") or (first == "physics" and second == "maths"):
    print("Suitable branch: Engineering")

elif (first == "maths" and second == "programming") or (first == "programming" and second == "maths"):
    print("Suitable branch: Computer Science")

elif (first == "biology" and second == "chemistry") or (first == "chemistry" and second == "biology"):
    print("Suitable branch: Biotechnology")

elif (first == "maths" and second == "statistics") or (first == "statistics" and second == "maths"):
    print("Suitable branch: Data Science")

else:
    print("No suitable branch found.")

