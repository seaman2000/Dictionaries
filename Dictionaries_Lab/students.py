students = {}

while True:
    line = input()

    if ":" not in line:
        searched_course = ' '.join(line.split("_"))
        break

    name, student_id, course = line.split(":")
    students[name] = (student_id, course)

for name, data in students.items():
    if data[1] == searched_course:
        print(f"{name} - {data[0]}")

