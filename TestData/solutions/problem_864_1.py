class Solution:
    def solution_864_1(self, N: List[int]) -> List[int]:
        L, A = len(N), []
        for i in range(0,L,2):
            A.extend(N[i]*[N[i+1]])
        return A