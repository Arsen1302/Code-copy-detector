class Solution:
    def solution_496_1_1(self, n: int) -> float:
        @cache                                 # cache the result for input (a, b)
        def solution_496_1_2(a, b):
            if a <= 0 and b > 0: return 1      # set criteria probability
            elif a <= 0 and b <= 0: return 0.5
            elif a > 0 and b <= 0: return 0
            return (solution_496_1_2(a-4, b) + solution_496_1_2(a-3, b-1) + solution_496_1_2(a-2, b-2) + solution_496_1_2(a-1, b-3)) * 0.25 # solution_496_1_2
        if n > 4275: return 1                  # observe the distribution you will find `a` tends to be easier to get used up than `b`
        n /= 25                                # reduce the input scale
        return solution_496_1_2(n, n)                       # both soup have `n` ml