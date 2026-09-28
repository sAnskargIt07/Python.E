# Experiment No. 5
# Calculate average grade of students

n = int(input("Enter number of students: "))

total_class_score = 0

for i in range(1, n + 1):
    print("\nEnter marks for Student", i)
    
    total = 0
    
    for j in range(1, 6):
        marks = float(input("Enter marks for Test " + str(j) + ": "))
        total += marks
    
    average = total / 5
    total_class_score += total
    
    print("Average of Student", i, "=", average)

overall_average = total_class_score / (n * 5)

print("\nOverall Average of the Class =", overall_average)