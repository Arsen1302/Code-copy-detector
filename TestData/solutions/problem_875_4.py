class Solution:
    def solution_875_4(self, n: int, arr: List[int]) -> int:
		#make array 'dp' to perform jump game II
        dp = [0]*(n+1)
        for i in range(n+1) :
            idxl = max(0, i-arr[i])
            idxr = min(n, i+arr[i])
            dp[idxl] = max(dp[idxl], idxr-idxl)
		# Now  just implement jump game II 
        if dp[0] == 0 :
            return -1;
        jump = dp[0]
        currjump = dp[0]
        res = 1
        for i in range(1, n+1) :
            currjump = max(currjump-1, dp[i])
            jump -= 1
            if jump == 0 and i != n :
                res += 1
                jump = currjump
            if jump == 0 and i < n :
                return -1
        return res