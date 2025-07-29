class Solution:
    def solution_623_3(self, s: str) -> List[int]:
        
        #two pointers start = 0 and (end)n = len(s)
        
        start = k = 0
        n =len(s)
        
        res=[None]*(n+1)

        for x in s:
            if x == "I":
                res[k]=(start)
                start+=1
            else:
                res[k]=(n)
                n-=1
            k+=1
        res[k]=start
        return res
    #i used k for faster complexity but you can use res.append(start or n) instead