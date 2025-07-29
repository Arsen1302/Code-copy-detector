class Solution:
    def solution_1385_1(self, s: str) -> int:
        ans = i = 0
        while i < len(s): 
            if s[i] == "X": 
                ans += 1
                i += 3
            else: i += 1
        return ans