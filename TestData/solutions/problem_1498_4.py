class Solution:
    def solution_1498_4(self, num: int) -> int:
        ans = 0 
        for x in range(1, num+1): 
            sm = sum(map(int, str(x)))
            if not sm&amp;1: ans += 1
        return ans