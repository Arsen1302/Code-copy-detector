class Solution:
    def solution_28_5(self, s: str, t: str) -> int:
        ls=len(s)
        lt=len(t)
        prev=[1]*(ls+1)


        for ind_t in range(1,lt+1):
            temp=[0]*(ls+1)
            for ind_s in range (1,ls+1):
                
                
                if s[ind_s-1]==t[ind_t-1]:
                    temp[ind_s]= prev[ind_s -1]+temp[ind_s -1] 
                    
                else:
                    temp[ind_s]= temp[ind_s -1]
                

            prev=temp  



        return prev[ind_s]