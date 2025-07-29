class Solution:
    def solution_595_3(self, N: List[int]) -> List[int]:
        L = len(N)
        for i in range(1,L):
            for j in range(0,i):
                if N[i] < N[j]:
                    N.insert(j, N.pop(i))
                    break
        return N