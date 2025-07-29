class Solution:
    def solution_1543_2(self, total: int, cost1: int, cost2: int) -> int:
        
        result = 0
        budget = total
        
        cost1, cost2 = sorted([cost1, cost2], reverse = True)
        
        for i in range((budget // cost1) + 1):
            budget = total
            budget -= (i * cost1)
            j = max(budget // cost2, 0)
            result += j + 1

        return result