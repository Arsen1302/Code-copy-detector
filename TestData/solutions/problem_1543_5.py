class Solution:
    def solution_1543_5(self, total: int, cost1: int, cost2: int) -> int:
        if cost1 < cost2:
            cost1, cost2 = cost2, cost1
        ans = 0
        for i in range(total // cost1 + 1):
            for _ in range((total - i * cost1) // cost2 + 1):
                ans += 1
        return ans