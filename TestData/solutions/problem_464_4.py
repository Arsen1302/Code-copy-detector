class Solution:
    def solution_464_4(self, jewels: str, stones: str) -> int:
        stones = list(stones)
        jewels = list(jewels)
        
        match = len([i for i in stones if i in jewels])
        
        return match