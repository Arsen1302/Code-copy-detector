class Solution:
    def solution_1640_3(self, edges: List[int]) -> int:
        sums = [0] * len(edges)
        for i, n in enumerate(edges):
            sums[n] += i
        return sums.index(max(sums))