class Solution:
    def solution_712_4_1(self, a: int, b: int, c: int):
        a, b, c = sorted([a,b,c])
        if a+1 == b == c-1: return [0,0]

        def solution_712_4_2(a,b,c):
            if a+1==b or b+1 == c or c-b==2 or b-a==2: return 1
            else: return 2

        def solution_712_4_3(a,c):
            return c-a-2

        return [solution_712_4_2(a,b,c), solution_712_4_3(a,c)]