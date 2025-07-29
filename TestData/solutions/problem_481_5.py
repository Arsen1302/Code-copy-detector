class Solution:
    def solution_481_5(self, S: str, T: str) -> str:
        x = ''
        t = {}
        for i in T:
            if i not in S:
                x += i
            t[i] = t.get(i,0) + 1
        for i in S:
            if i in T:
                x += i*t[i]
        return x