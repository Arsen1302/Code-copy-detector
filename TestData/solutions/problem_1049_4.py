class Solution:
    def solution_1049_4(self, n: int) -> str:
        if(len(str(n))<=3):
            return str(n)
        
        s = list(str(n))
        
        for i in range(len(s)-3,0,-3):
                s.insert(i,'.')
            
        ans = ''.join(s)
        return ans