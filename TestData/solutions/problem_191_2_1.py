class Solution:
    def solution_191_2_1(self, nums: List[int], target: int) -> int:
        
        dp = defaultdict(int)
        
        return self.solution_191_2_2(nums, target, dp)
    
    def solution_191_2_2(self, nums, target, dp):
        
        if target == 0:
            return 1
        
        if target < 0:
            return 0
        
        if target in dp:
            return dp[target]
        
        for num in nums:
            dp[target] += self.solution_191_2_2(nums, target-num, dp)
        
        return dp[target]