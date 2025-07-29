class Solution:
    def solution_1161_4(self, n: int) -> int:      
        if n<=7:
            return int(n*(n+1)/2)
        else:
            l = [i for i in range(1,8)]
            s=28
            while n>0:      
                n-=7
                l = [i+1 for i in l][:n]
                
                if n<=7:
                    s += sum(l)
                    return s
                else:
                    s += sum(l)
        return s