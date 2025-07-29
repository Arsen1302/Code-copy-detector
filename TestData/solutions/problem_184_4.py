class Solution:
    def solution_184_4(self, nums: List[int]) -> List[int]:
        # O(n^2) time
        nums.sort() # so that divisors appear ahead of each number
        n = len(nums)
        if n == 0: return []
        dp = [[num] for num in nums] # dp[i] represents the valid solution including nums[i]
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1: # find better solution, update
                    dp[i] = dp[j] + [nums[i]]
        return max(dp, key = len) # customer sort based on length