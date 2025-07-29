class Solution:
    def solution_939_5_1(self, s: List[int]) -> str:
        
        @cache
        def solution_939_5_2(pos = 0):
            if pos == len(s):
                return 0
            else:
                a = s[pos] - solution_939_5_2(pos + 1)
                b = -math.inf if pos + 1 >= len(s) else s[pos] + s[pos + 1] - solution_939_5_2(pos + 2)
                c = -math.inf if pos + 2 >= len(s) else s[pos] + s[pos + 1] + s[pos + 2] - solution_939_5_2(pos + 3)
                return max(a, b, c)
        ans = solution_939_5_2()
        
        return "Bob" if ans < 0 else "Alice" if ans > 0 else "Tie"