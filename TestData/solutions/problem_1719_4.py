class Solution:
    def solution_1719_4(self, nums: List[int], k: int) -> int:
     
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        
        result = 0
        
        for i in range(n-1,-1,-1):
            for j in range(i, n):
                
                temp = math.lcm(nums[i], nums[j])
                
                if i + 1 == j or i == j:
                    dp[i][j] = temp
                
                else:
                    dp[i][j] = math.lcm(temp, dp[i+1][j-1])
                
                if dp[i][j] == k:
                    result += 1
                       
                    
        return result