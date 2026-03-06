number_of_students = int(input())
students = {}

for _ in range(number_of_students):
    student_name = input()
    grade = float(input())
    students.setdefault(student_name, []).append(grade)

for name, grades in students.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        print(f"{name} -> {average_grade:.2f}")