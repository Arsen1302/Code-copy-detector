class Solution:
    def solution_1203_3(self, nums: List[int], multipliers: List[int]) -> int:
        # dp[i, left]: the maximum possible score if we have already done 'i' total operations 
        # and used 'left' numbers from the left side.
        # if we know the used 'left' numbers from the leftmost side, 
        # then the index of the rightmost element = n-1-(i-left)
        
        n = len(nums)
        m = len(multipliers)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        
		# why we move backwards (how to determine the order)?
        # 1. outer loop: we must move backwards because only in this way we can make full use of all the information we have met.
        # 2. inner loop: left must less of equal to i, so the inner loop move backwards.
        for i in range(m-1, -1, -1):
            for left in range(i, -1, -1):
                mult = multipliers[i]
                right = n - 1 - (i - left)
                # If we choose left, the the next operation will occur at (i + 1, left + 1)
                left_choice = mult * nums[left] + dp[i + 1][left + 1]
                # If we choose right, the the next operation will occur at (i + 1, left)
                right_choice = mult * nums[right] + dp[i + 1][left]
                dp[i][left] = max(left_choice, right_choice)       
        
        return dp[0][0]