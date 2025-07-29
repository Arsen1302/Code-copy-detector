class Solution:
    def solution_1335_5(self, s: str) -> str:
        stack = []
        count = 0

        while count < len(s):
            if stack == []:
                stack.append(s[count])
                count += 1
                continue
            elif len(stack) >= 2:
                if s[count] == stack[-1] and s[count] == stack[-2]:
                    stack.pop(-1)
            stack.append(s[count])
            count += 1

        return ''.join(stack)