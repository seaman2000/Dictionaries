exam_results = {}
submissions = {}

while True:
    submission = input()

    if submission == "exam finished":
        break
    parts = submission.split("-")
    if len(parts) == 2:
        name, command = parts
        if command == "banned":
            del exam_results[name]
    else:
        name, language, points = parts
        points = int(points)
        exam_results.setdefault(name, 0)
        submissions[language] = submissions.get(language, 0) + 1

        exam_results[name] = max(points, exam_results.get(name, 0))

print("Results:")
for username, points in exam_results.items():
    print(f"{username} | {points}")

print("Submissions:")
for language, count in submissions.items():
    print(f"{language} - {count}")
