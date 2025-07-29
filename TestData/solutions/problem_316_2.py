class Solution:
    def solution_316_2(self, a: str, b: str) -> str:
        [A1,B1,A2,B2] = map(int,(a+'+'+b).replace('i','').split('+'))
        return str(A1*A2-B1*B2)+'+'+str(A1*B2+A2*B1)+'i'
		
		
- Junaid Mansuri
- Chicago, IL