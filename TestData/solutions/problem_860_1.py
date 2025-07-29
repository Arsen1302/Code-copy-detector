class Solution:
    def solution_860_1(self, s: str) -> str:
        for i in range(26,0,-1): s = s.replace(str(i)+'#'*(i>9),chr(96+i))
        return s
            
		
		
- Junaid Mansuri
- Chicago, IL