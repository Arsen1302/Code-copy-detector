class Solution:
    def solution_1030_3(self, target: str) -> int:
        ans, prev = 0,"0"
        for c in target: 
            if prev != c: ans += 1
            prev = c
        return ans