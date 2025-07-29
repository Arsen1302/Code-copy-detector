class Solution:
    def solution_28_3_1(self, s: str, t: str) -> int:
        def solution_28_3_2(s,t,ind_s,ind_t,dp):
            if ind_t<0:
                return 1
            if ind_s<0:
                return 0


            if s[ind_s]==t[ind_t]:
                if (dp[ind_t])[ind_s]!=-1:
                    return (dp[ind_t])[ind_s]
                else:
                    (dp[ind_t])[ind_s]=(solution_28_3_2(s,t,ind_s-1,ind_t-1,dp) + solution_28_3_2(s,t,ind_s-1,ind_t,dp))
                    return (dp[ind_t])[ind_s]

            (dp[ind_t])[ind_s]=solution_28_3_2(s,t,ind_s-1,ind_t,dp)
            return (dp[ind_t])[ind_s]






        ls=len(s)
        lt=len(t)
        dp=[[-1]* ls for i in range(lt)]
        return solution_28_3_2(s,t,ls-1,lt-1,dp)