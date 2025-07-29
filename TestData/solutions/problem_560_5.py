class Solution:
    def solution_560_5(self, A: List[int]) -> int:
        seen = {}
        for i in range(len(A)):
            for j in range(i): 
                seen[A[i], A[j]] = 1 + seen.get((A[j], A[i] - A[j]), 1)
        ans = max(seen.values())
        return ans if ans >= 3 else 0