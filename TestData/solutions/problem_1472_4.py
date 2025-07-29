class Solution:
    def solution_1472_4(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        bought = res = 0
        for p in cost:
            if bought < 2:
                res += p
                bought += 1
            else:
                bought = 0
        return res