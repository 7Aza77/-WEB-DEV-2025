# Read number of students
n = int(input())

# Initialize dictionary to store student names and marks
student_marks = {}

# Read student data
for _ in range(n):
    data = input().split()
    name, scores = data[0], list(map(float, data[1:]))
    student_marks[name] = scores

# Query student name
query_name = input()

# Calculate average and print formatted result
average = sum(student_marks[query_name]) / len(student_marks[query_name])
print(f"{average:.2f}")