class Solution:
    def solution_600_2(self, s: str) -> str:
        
        y='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        one = 0
        
        two = len(s)-1
        
        s= list(s)
        
        while one < two:
            
            if s[one] in y:
                if s[two] in y:
                    s[one], s[two] = s[two] , s[one]
                    one+=1
                    two-=1
                else:
                    two-=1
            else:
                one+=1
        return ''.join(s)