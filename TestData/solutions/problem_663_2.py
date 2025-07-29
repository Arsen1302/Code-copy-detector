class Solution:
    def solution_663_2(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1]+1)
        date = 0 
        for idx in range(1,len(dp)):
            if idx == days[date]:
                one_day = dp[idx-1] + costs[0]
                seven_day = dp[idx-7] + costs[1] if idx - 7 >= 0 else costs[1]
                thirty_day = dp[idx-30] + costs[2] if idx - 30 >= 0 else costs[2]
                dp[idx] = min(one_day,seven_day,thirty_day)
                date += 1
            else:
                dp[idx] = dp[idx-1]
        return dp[-1]