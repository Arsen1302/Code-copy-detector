class Solution:
    def solution_614_1_1(self, nums):
        if len(nums) <= 2: return nums
        return self.solution_614_1_1(nums[::2]) + self.solution_614_1_1(nums[1::2])
    
    def solution_614_1_2(self, n: int) -> List[int]:
        return self.solution_614_1_1([i for i in range(1, n+1)])