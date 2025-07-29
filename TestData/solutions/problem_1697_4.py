class Solution:
    def solution_1697_4(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0 
        ii = imin = imax = -1
        for i, x in enumerate(nums): 
            if minK <= x <= maxK: 
                if minK == x: imin = i
                if maxK == x: imax = i 
                ans += max(0, min(imax, imin) - ii)
            else: ii = i
        return ans