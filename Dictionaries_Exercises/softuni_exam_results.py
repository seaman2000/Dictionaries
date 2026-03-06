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

        if points > exam_results[name].get(language, 0):
            exam_results[name] = points

print("Results:")
for username, points in exam_results.items():
    for language, value in points.items():
        print(f"{username} | {value}")

print("Submissions:")
for language, count in submissions.items():
    print(f"{language} - {count}")
