class Solution:
    def solution_514_5(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:

        res = 0
        for i in range(len(worker)):
            max_p = 0
            for j in range(len(difficulty)):
                if difficulty[j] <= worker[i]:
                    max_p = max(max_p, profit[j])
            res += max_p

        return res