class Solution:
    def solution_1247_5(self, costs: List[int], coins: int) -> int:
        costs = sorted(costs)
        total, ans = 0, 0   
        for cost in costs:
            if total + cost <= coins:
                total += cost
                ans += 1
            else:
                break
        return ans