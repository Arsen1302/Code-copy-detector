class Solution:
    def solution_1386_3(self, rolls, mean, n):
        m = len(rolls)
        sum_target = mean * (n + m)
        sum_current = sum(rolls)
        sum_remaining = sum_target - sum_current
        if not (n <= sum_remaining <= 6*n):
            return []
        
        remaining_rolls = [sum_remaining // n]*(n - sum_remaining % n) + [sum_remaining // n + 1]*(sum_remaining % n)
    
        return remaining_rolls