 
import sys
# Read 5 marks from command-line arguments
mark1 = float(sys.argv[1])
mark2 = float(sys.argv[2])
mark3 = float(sys.argv[3])
mark4 = float(sys.argv[4])
mark5 = float(sys.argv[5])

# Calculate average
average = (mark1 + mark2 + mark3 + mark4 + mark5) / 5

# Display results
print("\n--- Student Average Marks ---")
print(f"Marks: {mark1}, {mark2}, {mark3}, {mark4}, {mark5}")
print(f"Average Marks: {average:.2f}")
