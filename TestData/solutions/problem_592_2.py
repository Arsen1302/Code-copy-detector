class Solution:
    def solution_592_2(self, nums: List[int], k: int) -> int:
        if len(nums) <=1:
            return 0
        diff=max(nums)-min(nums)
		## diff after 
        new_diff=diff-2*k
        if new_diff < 0:
            return 0
        else:
            return new_diff