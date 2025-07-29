class Solution:
    def solution_910_5(self, s: str) -> int:
        indices = {a:i for i, a in enumerate('aeiou')}
        lefts = {0:-1}
        res = status = 0
        for right, a in enumerate(s):
            if a in indices:
                status ^= 1 << indices[a]
                if status not in lefts:
                    lefts[status] = right
            res = max(res, right - lefts[status])
            
        return res