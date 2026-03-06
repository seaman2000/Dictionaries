course_attempts = {}

while True:
    command = input()
    if command == "end":
        break
    course_name, student_name = command.split(" : ")
    course_attempts.setdefault(course_name, []).append(student_name)

for course, students in course_attempts.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")
