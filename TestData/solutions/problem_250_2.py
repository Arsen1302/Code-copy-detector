class Solution:
    def solution_250_2(self, s: str) -> str:
        ans = ''
        l = sorted(list(set(s)), key=s.count, reverse=True)
        for i in l:
            ans += i * s.count(i)
        return ans