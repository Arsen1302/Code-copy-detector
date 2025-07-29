class Solution:
    def solution_75_4(self, columnNumber: int) -> str: 
        
        if columnNumber==0:
            return ''
        
        q,r=divmod(columnNumber-1,26)
        
        return self.solution_75_4(q)+chr(r+ord('A'))