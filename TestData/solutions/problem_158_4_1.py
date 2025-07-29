class Solution:
    def solution_158_4_1(self, coins: List[int], amount: int) -> int:
        
        @cache
        def solution_158_4_2(x):
            """Return fewest number of coins to make up to x."""
            if x == 0: return 0
            if x < 0: return inf
            return min(1 + solution_158_4_2(x - coin) for coin in coins)
        
        return solution_158_4_2(amount) if solution_158_4_2(amount) < inf else -1