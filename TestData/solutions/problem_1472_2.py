class Solution:
    def solution_1472_2(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        res, idx, N = 0, 0, len(cost)
        while idx < N:
            res += sum(cost[idx : idx + 2])
            idx += 3
        return res