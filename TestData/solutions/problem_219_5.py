class Solution:
    def solution_219_5(self, s: str) -> int:
        
        dic ={}
        res = 0
        odd = False
        
        for i in s:
            dic.update({i:s.count(i)})
        
        for key,value in dic.items():
            if value%2==0:
                res += value
            else:
                res += value - 1
                odd = True
                
        if odd:
            return res+1
        else:
            return res