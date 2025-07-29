class Solution:
    def solution_396_5(self, nums: List[int]) -> int:
        dp = [0] * len(nums) # longest subseq
        cdp = [0] * len(nums) # count of longest subseq
        
        longest = 1
        
        for i in range(len(nums)):
            dp[i] = 1
            cdp[i] = 1
            
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[i] < dp[j] + 1: # found new longest seq
                        dp[i] = dp[j] + 1 # update seq len for cur idx
                        cdp[i] = cdp[j] # update count of longest seq (same as prev longest count seq because we only update len, for every prev longest can add one digit => general count longest seq are not change)
                    elif dp[i] == dp[j] + 1: # found new way to achieve longest seq
                        cdp[i] += cdp[j] # increase general count longest seq

                longest = max(longest, dp[i])
        
        res = 0
        for idx in range(len(dp)): # finally sum all count of longest seqs
            if dp[idx] == longest:
                res += cdp[idx]

        return res