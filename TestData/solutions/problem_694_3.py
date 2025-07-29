class Solution:
    def solution_694_3(self, values: List[int]) -> int:
        n = len(values)
        maximum = 0
        for i in range(n):
            for j in range(i+1, n):
                if i >= j: continue
                maximum = max(maximum, values[i] + values[j] + i - j)
        return maximum