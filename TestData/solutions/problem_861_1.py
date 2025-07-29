class Solution:
    def solution_861_1(self, A: List[int], Q: List[List[int]]) -> List[int]:
        B = [A[0]]
        for a in A[1:]: B.append(B[-1]^a)
        B.append(0)
        return [B[L-1]^B[R] for L,R in Q]