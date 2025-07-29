class Solution:
    def solution_1197_2(self, s: str) -> str:
        if not s: return "" # boundary condition 
        ss = set(s)
        for i, c in enumerate(s):
            if c.swapcase() not in ss: 
                s0 = self.solution_1197_2(s[:i])
                s1 = self.solution_1197_2(s[i+1:])
                return max(s0, s1, key=len)
        return s