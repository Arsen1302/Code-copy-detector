class Solution:
    def solution_1144_4(self, cuboids: List[List[int]]) -> int:
        n = len(cuboids)
        
        dp = [0]*n
        for c in cuboids:
            c.sort()
        cuboids.sort()
        
        for i in range(n):
            dp[i] = cuboids[i][2]
            for j in range(i):
                if cuboids[j][1] <= cuboids[i][1] and cuboids[j][2] <= cuboids[i][2]:
                    dp[i] = max(dp[i],dp[j]+cuboids[i][2])
                    
        return max(dp)