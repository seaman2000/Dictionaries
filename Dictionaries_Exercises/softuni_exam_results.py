exam_results = {}
while True:
    submission = input()
    if submission == "exam finished":
        break
    name, language, points = submission.split("-")
    points = int(points)
    exam_results.setdefault(name, {})
    if points > exam_results[name].get(language, 0):
        exam_results[name][language] = points

print(exam_results)