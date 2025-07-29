class Solution:
    def solution_1161_2_1(self, n: int) -> int:
        def solution_1161_2_2(days, n=1, wek=7):
            res = 0
            for day in range(n, days+n):
                res += day
                print(day)
                if day == wek:
                    return res + solution_1161_2_2(days-7, n+1, wek+1)
            return res
        return solution_1161_2_2(n)