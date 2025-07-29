class Solution:
    def solution_714_2(self, nums1: List[int], nums2: List[int]) -> int:
        m=len(nums1)
        n=len(nums2)
        dp=[]
        for i in range (m+1):
            dp.append([0]*(n+1))
        #print(dp)
        cnt=0
        for i in range (m+1):
            dp[i][0]=0
        for i in range (n+1):
            dp[0][i]=0
        for i in range (1,m+1):
            for j in range (1,n+1):
                if nums1[i-1]==nums2[j-1]:
                    dp[i][j]=max((dp[i-1][j-1]+1),max(dp[i-1][j],dp[i][j-1]))
                else:
                    dp[i][j]=max(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])

        return dp[-1][-1]