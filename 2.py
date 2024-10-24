def solve(s):
    stack = []
    tag_name = []
    is_closing_tag = False
    for i in s:
        if i == '<': pass
        elif i == '>':
            tag_name = ''.join(tag_name)
            if is_closing_tag:
                if not stack:
                    return False
                if stack[-1] != tag_name:
                    return False
                stack.pop()
                is_closing_tag = False
            else:
                stack.append(tag_name)
            tag_name = []
        elif i == '/':
            is_closing_tag = True
        else:
            tag_name += i
    return not stack


testcases = ["<div><p></div></p>", "<div><p></p></div>", "<div></p><p></div>", "<div><p></div>", "<></>"]
for i in testcases:
    print(f'{i}\t{solve(i)}')