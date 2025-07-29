class Solution:
    def solution_1276_3_1(self, s: str) -> int:
        def solution_1276_3_2(t):
            return len(set(t)) == 3
        
        return sum(map(solution_1276_3_2, zip(s, s[1:], s[2:])))