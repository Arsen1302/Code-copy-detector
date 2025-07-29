class Solution:
    def solution_111_5(self, s: str) -> int:
        ans, sign, val = 0, 1, 0
        stack = []
        for c in s:
            if c.isdigit():
                val = 10*val + int(c)
            elif c in "+-":
                ans += sign * val 
                val = 0
                sign = 1 if c == "+" else -1
            elif c == "(":
                stack.append(ans)
                stack.append(sign)
                ans, sign = 0, 1
            elif c == ")":
                ans += sign * val 
                ans *= stack.pop() 
                ans += stack.pop()
                val = 0
        return ans + sign * val