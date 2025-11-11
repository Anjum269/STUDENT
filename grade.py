 import sys

# Student Grade Evaluation Program

# Use default marks if no arguments are provided
if len(sys.argv) == 1:
    marks = [80, 35, 89, 67, 97]
elif len(sys.argv) == 6:
    marks = [float(mark) for mark in sys.argv[1:]]
else:
    print("Invalid number of arguments. Please provide 5 marks or none.")
    sys.exit(1)

# Calculate average
average = sum(marks) / 5

# Determine grade
if average >= 90:
    grade = 'A'
elif average >= 75:
    grade = 'B'
elif average >= 60:
    grade = 'C'
elif average >= 40:
    grade = 'D'
else:
    grade = 'Fail'

# Display results
print("\n--- Student Grade Evaluation ---")
print(f"Marks: {marks}")
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")
