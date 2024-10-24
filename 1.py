class Token:
    pass

class Number(Token):
    def __init__(self, n):
        self.val = n

class Operator(Token):
    def __init__(self, o):
        self.val = o


def tokenize(s):
    tokens: list[Token] = [Number(0)]
    for i in s:
        if i in '1234567890':
            if type(tokens[-1]) == Operator:
                tokens.append(Number(int(i)))
            elif type(tokens[-1]) == Number:
                tokens[-1].val = tokens[-1].val * 10 + int(i)
        else:
            tokens.append(Operator(i))
    return tokens


def calculate(tokens: list[Token]):
    stack = []
    first = tokens[0].val
    stack.append(first)
    for i in range(1, len(tokens) - 1, 2):
        op = tokens[i].val
        second = tokens[i + 1].val
        if op in '+-':
            first = stack.pop()
            stack.append(op)
            stack.append(first)
            stack.append(second)
        elif op in '*/':
            first = stack.pop()
            if op == '*':
                stack.append(first*second)
            else:
                stack.append(int(first/second))
    while len(stack) > 1:
        second = stack.pop()
        first = stack.pop()
        op = stack.pop()
        if op == '-':
            stack.append(first - second)
        else:
            stack.append(first + second)
    return stack[0]


print(calculate(tokenize('22+2*4+2/2*4')))