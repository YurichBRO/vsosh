def to_binary(n):
    result = []
    while n:
        result.append(n & 1)
        n >>= 1
    return ''.join(map(str, result))[::-1]

def from_binary(n):
    result = 0
    for i in n:
        result = result * 2 + int(i)
    return result

print(from_binary("1010"))