class Solution:
    def solution_1240_4(self, n: int, k: int) -> int:
        l = list(range(n))
        s = 0
        while len(l) > 1:
            i = (k%len(l) + s)%len(l)
            l = l[: i] + l[i+1: ]
            s = i-1
        return l[0] or n