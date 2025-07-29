class Solution:
    def solution_306_5(self, A: str, B: str) -> int:
        if A == B:
            return -1
        return max(len(A), len(B))