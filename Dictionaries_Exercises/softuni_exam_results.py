exam_results = {}
submissions = {}

while True:
    submission = input()

    if submission == "exam finished":
        break

    name, language, points = submission.split("-")
    if points == "banned":
        del exam_results[name]
        continue

    points = int(points)
    exam_results.setdefault(name, {})
    submissions[language] = submissions.get(language, 0) + 1

    if points > exam_results[name].get(language, 0):
        exam_results[name][language] = points

print("Results:")
for username, points in exam_results.items():
    for language, value in points.items():
        print(f"{username} | {value}")

for language, count in submissions.items():
    print(f"{language} - {count}")
