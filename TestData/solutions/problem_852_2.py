class Solution:
    def solution_852_2(self, A: List[int]) -> List[int]:
        for i in range(len(A)-2,-1,-1): A[i] = max(A[i],A[i+1])
        return  A[1:]+[-1]
		
- Junaid Mansuri
- Chicago, IL