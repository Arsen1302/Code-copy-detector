class Solution:
    def solution_997_3(self, n: int, start: int) -> int:
        ans = start
        for i in range(1 , n):
            ans ^= start + (2 * i)
        
        return ans