class Solution:
    def solution_601_2_1(self, nums: List[int]) -> int:
        
        def solution_601_2_2( A: List[int]) -> int:
        
            size = len(A)
            
            dp = [ 0 for _ in range(size)]
            dp[0] = A[0]

            for i in range(1, size):

                dp[i] = max(dp[i-1] + A[i], A[i])

            return max(dp)
        
        # -----------------------------------------------------------
        
        ## Boundary case, only one element
        if len(nums) == 1:
            return nums[0]
        
        ## General cases:
        
        # Maximal without first element
        drop = solution_601_2_2(nums[1:])
        
        # Maxiaml with first element selected
        pick = sum(nums) + max(0, solution_601_2_2([-number for number in nums[1:]]))
        
        return max(drop, pick)