class Solution:
    def solution_864_2(self, N: List[int]) -> List[int]:
        return sum([N[i]*[N[i+1]] for i in range(0,len(N),2)],[])
		
		
- Junaid Mansuri
- Chicago, IL