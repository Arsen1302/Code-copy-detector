class Solution:
    def solution_518_5(self, s: str) -> List[List[int]]:
        start = 0
        cur = s[0]
        res = []

        for i, c in enumerate(s[1:] + ' ', start=1):
            if c != cur:
                if i - start >= 3:
                    res.append([start, i-1])
                start = i
                cur = c
        
        return res