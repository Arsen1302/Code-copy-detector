class Solution:
    def solution_399_2(self, s: str) -> bool:
        leftmin = leftmax = 0
        for c in s:
            if c == "(":
                leftmax += 1
                leftmin += 1
            if c == ")":
                leftmax -= 1
                leftmin = max(0, leftmin-1)
            if c == "*":
                leftmax +=1
                leftmin = max(0, leftmin-1)
            if leftmax < 0:
                return False
        if leftmin == 0:
            return True