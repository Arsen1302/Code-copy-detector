class Solution:
    def solution_1472_3(self, cost: List[int]) -> int:
        return sum(x for i, x in enumerate(sorted(cost, reverse=True)) if (i+1)%3)