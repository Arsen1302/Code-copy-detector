class Solution:
    def solution_1482_5(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        end = 0
        start = 0
        total = 0
        powr = 1
        for i in range(k):
            
            total = total + ((ord(s[end]) - ord('a') + 1)) * powr
            powr = powr * power
            end +=1
            
            
        res = total % modulo
        
        if res == hashValue:
            return s[start:end]
        
        
        start = 1
        end = k
        powr = powr // power 
        while end < len(s):
            
            total = total - ((ord(s[start-1]) - ord('a') +1))
            total //=power
            
            total = total + ((ord(s[end]) - ord('a') +1) * powr)

            if total % modulo == hashValue:
                return s[start:end+1]
                
                
            end +=1
            start +=1