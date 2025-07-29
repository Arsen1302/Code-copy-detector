class Solution:
    def solution_87_1_1(self):
        self.cache = {}
        
    def solution_87_1_2(self, nums, start):
        if start >= len(nums):
            return 0
        
        if start in self.cache:
            return self.cache[start]
        
        self.cache[start] = nums[start] + max(self.solution_87_1_2(nums, start+2), self.solution_87_1_2(nums, start+3))
        return self.cache[start]
        
    def solution_87_1_3(self, nums: List[int]) -> int:
        return max(self.solution_87_1_2(nums, 0), self.solution_87_1_2(nums, 1))