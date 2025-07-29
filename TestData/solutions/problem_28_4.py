class Solution:
    def solution_28_4(self, s: str, t: str) -> int:
        ls=len(s)
        lt=len(t)
        dp=[[0]*(ls+1) for i in range(lt+1)]
        for i in range(ls):
            (dp[0])[i]=1

        for ind_t in range(1,lt+1):
            for ind_s in range (1,ls+1):
                if s[ind_s-1]==t[ind_t-1]:
                    (dp[ind_t])[ind_s]= (dp[ind_t -1])[ind_s -1] +(dp[ind_t])[ind_s -1] 
                else:
                    (dp[ind_t])[ind_s]= (dp[ind_t])[ind_s -1]
                



        return (dp[ind_t])[ind_s]