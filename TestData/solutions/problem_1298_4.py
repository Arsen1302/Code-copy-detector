class Solution:
    def solution_1298_4(self, num: str) -> str:
        for i in reversed(range(len(num))):
            if int(num[i]) &amp; 1: return num[:i+1]
        return ""