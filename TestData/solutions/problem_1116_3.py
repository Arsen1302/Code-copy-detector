class Solution:
    def solution_1116_3(self, s: str) -> int:
        count = 0
        stack = []        
        for c in s:
            if c == 'b':
                stack.append(c)
            elif stack:
                stack.pop()
                count += 1
        return count