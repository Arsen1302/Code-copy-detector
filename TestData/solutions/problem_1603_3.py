class Solution:
    def solution_1603_3(self, n: int) -> int:
        if n == 1:
            return 4
        t = [0 for _ in range(n)]
        t[0], t[1] = 2, 3
        for i in range(2, n):
            t[i] = (t[i-1]+t[i-2])%(10**9 + 7)
        return t[n-1]**2%(10**9 + 7)