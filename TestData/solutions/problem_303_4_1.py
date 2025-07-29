class Solution:
    def solution_303_4_1(self, amount: int, coins: List[int]) -> int:
        coins.sort(reverse=True)
        
        @lru_cache(None)
        def solution_303_4_2(i, target):
            """Return number of number of combo in coins[i:] to make up target"""
            if target < 0: return 0
            if target == 0: return 1
            return sum(solution_303_4_2(k, target-coins[k]) for k in range(i, len(coins)))
        
        return solution_303_4_2(0, amount)