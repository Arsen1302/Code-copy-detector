class Solution:
    def solution_189_4(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for length in range(2, n + 1):
            for left in range(1, n - length + 2):
                right = left + length - 1
                dp[left][right] = float('inf')
                for k in range(left + 1, right):
                    dp[left][right] = min(dp[left][right], max(dp[left][k - 1], dp[k + 1][right]) + k)
                if left + 1 = right:
                    dp[left][left + 1] = left
        return dp[1][n]
    #the idea of my solution is to find the best case in worst case. what does it mean? 
    #we know the big interval relys on small interval, so we will only study the smallest case
    #if the interval is 0, dp[i][i] what is the value of this interval? it has to be 0, because you dont need to guess
    #what if the interval is 2, impossible to have interval 1, interval is 2 the value should be the smaller number
    #lets look at this example: [1,2] [2,3] you definatly gonna pick the cheap one, because after you pick one the answer
    #will be the another. 
    #because all the even interval will rely on the dp of interval 2, so once the dp[i][i + 1] is solved, the whole problem is solved !