class Solution:
    def solution_1472_1(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        res, i, N = 0, 0, len(cost)
        while i < N:
            res += sum(cost[i : i + 2])
            i += 3
        return res