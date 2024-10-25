class Solution:
    def longestValidParentheses(self, s: str) -> int:
        balance = 0
        length = 0
        stack = []
        index = 0
        max_length = 0
        for i in s:
            if i == "(":
                balance += 1
                stack.append(index)
            else:
                balance -= 1
                stack.pop()
                if balance < 0:
                    max_length = max(max_length, length)
                    length = -1
                    index = -1
            length += 1
            index += 1


tests = ["(()(()", ")()())", "))))())()()(()"]

for i in tests:
    print(Solution().longestValidParentheses(i))

