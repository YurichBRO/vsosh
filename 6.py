def solve(words):
    result = {}
    for i in words:
        length = len(i)
        if length in result:
            result[length].append(i)
        else:
            result[length] = [i]
    return result


print(solve(['word', 'another', 'hell']))