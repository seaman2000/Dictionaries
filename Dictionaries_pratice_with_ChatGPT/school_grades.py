students = {
    "Ivan": {"math": 5, "english": 4},
    "Maria": {"math": 6, "english": 6},
    "Georgi": {"math": 4, "english": 5}
}

for name, grades in students.items():
    if name == "Maria":
        print(students["Maria"])
    elif name == "Ivan":
        grade = students["Ivan"].values()
        avg_grade = sum(grade) / len(students["Ivan"])
        print(avg_grade)

highest_math_score = float("-inf")
name_of_student = ""

for name, grade in students.items():
    if grade["math"] > highest_math_score:
        highest_math_score = grade["math"]
        name_of_student = name

print(name_of_student, highest_math_score)