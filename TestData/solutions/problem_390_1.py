class Solution:
    def solution_390_1(self, n: int, k: int) -> List[int]:
        lo, hi = 1, n 
        ans = []
        while lo <= hi: 
            if k&amp;1: 
                ans.append(lo)
                lo += 1
            else: 
                ans.append(hi)
                hi -= 1
            if k > 1: k -= 1
        return ans