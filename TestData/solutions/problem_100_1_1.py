class Solution:
    def solution_100_1_1(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        dp = {}
        def solution_100_1_2(a,i):
            if i>=len(a):
                return 0
            if i in dp:
                return dp[i]
            
            sum = 0
            if i<len(a)-1:
                sum+= max(a[i]+solution_100_1_2(a,i+2),a[i+1]+solution_100_1_2(a,i+3))
            else:
                sum+=a[i]+solution_100_1_2(a,i+2)
            dp[i] = sum
            return sum
            
        x = solution_100_1_2(nums[:len(nums)-1],0)
        dp = {}
        y = solution_100_1_2(nums[1:],0)
            
        return max(x, y)