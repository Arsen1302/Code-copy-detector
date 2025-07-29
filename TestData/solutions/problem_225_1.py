class Solution:
    def solution_225_1(self, nums: List[int]) -> bool:
	    if sum(nums)%2:  # or if sum(nums)&amp;1
		    return False
		# main logic here