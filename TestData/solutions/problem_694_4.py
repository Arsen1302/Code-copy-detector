class Solution:
    def solution_694_4(self, values: List[int]) -> int:
        n = len(values)
        i = maximum = 0
        for j in range(i+1, n):
            maximum = max(maximum, values[i] + values[j] + i - j)
            if values[j] + j - i > values[i]: i = j
        return maximum