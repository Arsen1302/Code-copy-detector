class Solution:
    def solution_1144_1(self, cuboids: List[List[int]]) -> int:
        cuboids = sorted([sorted(cub) for cub in cuboids], reverse=True)   # sort LxWxH in cube, then sort cube reversely
        ok = lambda x, y: (x[0] >= y[0] and x[1] >= y[1] and x[2] >= y[2]) # make a lambda function to verify whether y can be put on top of x
        n = len(cuboids)
        dp = [cu[2] for cu in cuboids]                                     # create dp array
        ans = max(dp)
        for i in range(1, n):                                              # iterate over each cube
            for j in range(i):                                             # compare with previous calculated cube
                if ok(cuboids[j], cuboids[i]):                             # update dp[i] if cube[i] can be put on top of cube[j]
                    dp[i] = max(dp[i], dp[j] + cuboids[i][2])              # always get the maximum
            ans = max(ans, dp[i])                                          # record the largest value
        return ans