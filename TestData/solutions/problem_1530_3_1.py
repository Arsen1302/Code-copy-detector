class Solution:
    def solution_1530_3_1(self, nums: List[int]) -> List[int]:
        dp = []
        i = 0
        while i < len(nums) - 1:
            dp.append((nums[i] + nums[i + 1]) % 10)
            i += 1
        return dp
    
    def solution_1530_3_2(self, nums: List[int]) -> int:
        while len(nums) > 1:
            nums = self.solution_1530_3_1(nums)
        return nums[0]