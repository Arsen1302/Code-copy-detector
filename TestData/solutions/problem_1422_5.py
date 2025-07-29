class Solution:
    def solution_1422_5(self, colors: List[int]) -> int:
        n = len(colors)
        if n < 2:
            return 0 
        if colors[0]!=colors[-1]:
            return n-1
        d = 0
        for i in range(n):
            if colors[i] != colors[0]:
                d = max(d,i)
            if colors[i] != colors[-1]:
                d = max(d,n-1-i)
        return d