class Solution: 
    def solution_1644_1(self, s: str) -> int:
        ans = prefix = prev = 0 
        for i, ch in enumerate(s): 
            if ch == '1': 
                ans = max(prev, i - prefix)
                prefix += 1
                if ans: prev = ans+1
        return ans