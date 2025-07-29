class Solution:
    def solution_1144_5(self, cuboids: List[List[int]]) -> int:
        for cuboid in cuboids:
            cuboid.sort()
        cuboids.sort()
        n = len(cuboids)   
        dp = [height for _, _, height in cuboids]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if cuboids[i][1] <= cuboids[j][1] and cuboids[i][2] <= cuboids[j][2]:
                    dp[i] = max(dp[i], cuboids[i][2] + dp[j])
        
        return max(dp)