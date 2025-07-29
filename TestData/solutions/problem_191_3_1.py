class Solution:
    def solution_191_3_1(self, nums: List[int], target: int) -> int:
        '''
            Here we are doing bottom up DP and the base case would be =>
            when target is zero how many way can we achieve that: 1 way
        '''
        dp = { 0 : 1 } # base case 
        for total in range(1,target+1):
            dp[total] = 0
            for n in nums:
                dp[total] += dp.get(total-n,0)
        return dp[target]
                
        
    # /////// Solution 1 ///////
    def solution_191_3_2(self, nums, target, combination, lookup):
        if target == 0:
            return 1
        if target < 0:
            return 0
        if target not in lookup:
            ans = 0
            for num in nums:
                ans += self.solution_191_3_2(nums, target-num, combination+[num], lookup)
            lookup[target] = ans
        return lookup[target]
    
    def solution_191_3_1(self, nums: List[int], target: int) -> int:
        nums.sort()
        return self.solution_191_3_2(nums, target, [], {})