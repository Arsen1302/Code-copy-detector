class Solution:
    def solution_694_5(self, values: List[int]) -> int:
        i = best = 0
        for j in range(1, len(values)):
            best = max(best, values[i] + values[j] + i - j)
            if values[j] - i >= values[i] - j:
                i = j
        return best