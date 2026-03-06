exam_results = {}
while True:
    submission = input()
    if submission == "exam finished":
        break
    name, language, points = submission.split("-")
    points = int(points)
    exam_results[name] = {language: 0}
    if points > exam_results[name][language]:
        exam_results[name][language] = points

print(exam_results)