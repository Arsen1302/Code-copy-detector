class Solution:
    def solution_86_1(self, n: int) -> int: 
        return sum((n &amp; (1<<i))!=0 for i in range(32))