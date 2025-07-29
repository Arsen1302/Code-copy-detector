class Solution:
    def solution_1312_4(self, n: int) -> int:
        dt = defaultdict(lambda:0)
        res = 0
        for i in range(n+1):
            dt[i*i] = i
        for i in range(1,n-1):
            for j in range(i+1,n):
                if dt[(i*i)+(j*j)]:
                    res+=2
        return res