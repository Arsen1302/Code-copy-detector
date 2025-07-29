class Solution:
def solution_1542_3(self, nums: List[int]) -> int:
        res=[abs(ele) for ele in nums]
        a=(min(res))
        if a in nums:
            return a
        else:
            return a*-1