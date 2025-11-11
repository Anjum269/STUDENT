import sys

# Student Average Marks Program

# Take 5 marks as input
mark1 = float(input("Enter marks of subject 1: "))
mark2 = float(input("Enter marks of subject 2: "))
mark3 = float(input("Enter marks of subject 3: "))
mark4 = float(input("Enter marks of subject 4: "))
mark5 = float(input("Enter marks of subject 5: "))

# Calculate average
average = (mark1 + mark2 + mark3 + mark4 + mark5) / 5

# Display result
print("\n--- Student Average Marks ---")
print(f"Marks: {mark1}, {mark2}, {mark3}, {mark4}, {mark5}")
print(f"Average Marks: {average:.2f}")
