class Solution:
    def solution_1637_5(self, nums: List[int]) -> bool:
        a  = nums
        dp = [False] * len(a)
        for i in range(1, len(a)):
            ret = False
            if i-1>=0 and a[i]==a[i-1]:
                ret = ret or (True if i-2<0 else dp[i-2])
            if i-2>=0 and a[i]==a[i-1] and a[i-1]==a[i-2]:
                ret = ret or (True if i-3<0 else dp[i-3])
            if i-2>=0 and a[i]==a[i-1]+1 and a[i-1]==a[i-2]+1:
                ret = ret or (True if i-3<0 else dp[i-3])
            dp[i] = ret
        ans = dp[-1]
        return ans