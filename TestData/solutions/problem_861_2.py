class Solution:
    def solution_861_2(self, A: List[int], Q: List[List[int]]) -> List[int]:
        B = list(itertools.accumulate(A, func = operator.xor)) + [0]
        return [B[L-1]^B[R] for L,R in Q]
		
		
		
- Junaid Mansuri
- Chicago, IL