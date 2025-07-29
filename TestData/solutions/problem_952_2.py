class Solution:
    def solution_952_2(self, s: str) -> int:
        
        return max([s[:i].count('0')+s[i:].count('1') for i in range(1, len(s))])