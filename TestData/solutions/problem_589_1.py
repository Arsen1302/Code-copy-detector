class Solution:
    def solution_589_1(self, A: List[int]) -> List[int]:
        i, j = 0, len(A) - 1
        while i < j:
        	if A[i] % 2 == 1 and A[j] % 2 == 0: A[i], A[j] = A[j], A[i]
        	i, j = i + 1 - A[i] % 2, j - A[j] % 2
        return A