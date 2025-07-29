class Solution:
    
    def solution_87_2_1(self):
        self.cache = {}
    
    def solution_87_2_2(self, nums, current):
        if current < 0: # Beyond array boundary
            return 0
        
        try:
            return self.cache[current]
        except:
        
            self.cache[current] = max(self.solution_87_2_2(nums, current - 1),
                                      nums[current] + self.solution_87_2_2(nums, current - 2))
        return self.cache[current]
    
    def solution_87_2_3(self, nums: List[int]) -> int:
        return self.solution_87_2_2(nums, len(nums) - 1)