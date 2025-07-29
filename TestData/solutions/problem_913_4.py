class Solution:
    def solution_913_4(self, n: int) -> str:
        if(n % 2 == 0): return 'a' + 'b' * (n - 1)
        
        return 'a' * n