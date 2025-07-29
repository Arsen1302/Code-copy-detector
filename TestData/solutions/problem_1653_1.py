class Solution:
    def solution_1653_1(self, garbage: List[str], travel: List[int]) -> int:
        ans = sum(map(len, garbage))
        prefix = list(accumulate(travel, initial=0))
        for ch in "MPG": 
            ii = 0 
            for i, s in enumerate(garbage): 
                if ch in s: ii = i 
            ans += prefix[ii]
        return ans