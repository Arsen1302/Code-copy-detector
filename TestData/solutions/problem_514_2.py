class Solution:
    def solution_514_2(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # sort difficulty and profit together as a tuple
        difficulty, profit = zip(*sorted(zip(difficulty, profit)))
        ret = max_profit = idx = 0
        for ability in sorted(worker):
            # if ability is smaller than the smallest difficulty
            # it's smaller than all difficulties
            if ability < difficulty[0]: continue
            # try to find a larger profit than the current one
            # this while loop will be run for at most len(difficulty) times
            # as idx is not reset at the end
            while idx < len(difficulty) and ability >= difficulty[idx]:
                max_profit = max(max_profit, profit[idx])
                idx += 1
            # increment total profit
            ret += max_profit
        return ret