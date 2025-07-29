class Solution:
    def solution_179_3(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        dp=[]
        
        for _,h in envelopes:
            index = bisect.bisect_left(dp,h)
            
            if index < len(dp):
                dp[index] = h
            else:
                dp.append(h)
        
        return len(dp)