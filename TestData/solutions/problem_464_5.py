class Solution:
    def solution_464_5(self, jewels: str, stones: str) -> int:
        return len([i for i in list(stones) if i in list(jewels)])