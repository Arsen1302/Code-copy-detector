class Solution:
    def solution_582_1(self, A: List[int]) -> bool:
        if A[-1] < A[0]: 
            A = A[::-1]
        
        for i in range(1, len(A)):
            if A[i] < A[i-1]:
                return False
        return True