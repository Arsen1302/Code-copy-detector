class Solution:
    def solution_1476_4(self, nums: List[int]) -> int:
        min_=min(nums)
        max_=max(nums)
        c=0
        for i in nums:
            if min_<i<max_:
                c+=1
        return c