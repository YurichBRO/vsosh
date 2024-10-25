def solve(students):
    return sorted(sorted(students, key=lambda x: x['name']), key=lambda x: x['grade'])

print(solve([{'name': 'b', 'grade': 2}, {'name': 'b', 'grade': 1}, {'name': 'a', 'grade': 1}]))