students = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

scores = sorted(set([score for name, score in students]))
second_lowest = scores[1]

second_lowest_names = sorted([name for name, score in students if score == second_lowest])


for name in second_lowest_names:
    print(name)
