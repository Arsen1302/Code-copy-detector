class Solution:
    def solution_1003_5(self, nums: List[int]) -> int:
        zeroPos = []
        n = len( nums)
        ct = 0
        dp = []
        
        for i in range ( n):
            if nums[i] == 1:
                ct += 1
                dp.append(ct)
            else:
                ct = 0
                dp.append(ct)
                zeroPos.append(i)
        
        zn = len( zeroPos)
        
        if zn == 0:
            return n-1
        if zn == n:
            return 0
        
        realMax = 0
        
        for i in range ( zn):
            val1 = dp[zeroPos[i]]
            val2 = dp[zeroPos[i]]
            
            if zeroPos[i] > 0:
                val1 = dp[zeroPos[i]-1]
                val2 = 0

                if zeroPos[i]+1 < n:
                    val2 = dp[zeroPos[i]+1]
                if i < zn-1:
                    val2 = dp[zeroPos[i+1]-1]
                if i == zn-1:
                    val2 = dp[n-1]
            realMax = max( realMax, val1+val2)
        return realMax
		```