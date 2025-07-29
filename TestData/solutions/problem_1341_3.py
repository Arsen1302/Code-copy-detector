class Solution:
    def solution_1341_3(self, s: str) -> int:
        ans = prefix = 0 
        for ch in s:
            if ch == "[": prefix += 1
            else: prefix -= 1
            if prefix == -1:
                ans += 1
                prefix = 1
        return ans