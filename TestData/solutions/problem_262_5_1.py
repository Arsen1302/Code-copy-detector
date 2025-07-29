class Solution:
    def solution_262_5_1(self, maxChoosableInteger: int, desiredTotal: int) -> bool:

        @lru_cache(maxsize=None)
        def solution_262_5_2(choices, remainder):
            if choices[-1] >= remainder: return True

            for index in range(len(choices)):
                if not solution_262_5_2(choices[:index] + choices[index + 1:], remainder - choices[index]): return True

            return False

        summed_choices =  maxChoosableInteger * (maxChoosableInteger + 1) / 2
        if summed_choices < desiredTotal: return False
        if summed_choices == desiredTotal: return maxChoosableInteger % 2

        return solution_262_5_2(tuple(range(1, maxChoosableInteger + 1)), desiredTotal)