class Solution:
    def solution_319_4(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            if i%2:  # alternate between +ve and -ve
                result -= nums[i]
            else:
                result += nums[i]
        return result
		# return sum((-1)**i*v for i,v in enumerate(nums))  # one-liner