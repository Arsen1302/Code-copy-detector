class Solution:
    def solution_400_5_1(self, s: str) -> bool:
        def solution_400_5_2(s):
            lo, hi = 0, len(s) - 1
            while lo < hi:
                if s[lo] != s[hi]: return False
                lo += 1
                hi -= 1
            return True
        
        lo, hi = 0, len(s) - 1
        while lo < hi:
            if s[lo] != s[hi]:
                return solution_400_5_2(s[lo+1:hi+1]) or solution_400_5_2(s[lo:hi])
            lo += 1
            hi -= 1
        return True