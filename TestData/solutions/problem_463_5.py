class Solution:
    def solution_463_5(self, arr: List[int]) -> int:
        start, max_value, chunks = 0, 0, 0
        for index, value in enumerate(arr):
            max_value = max(value, max_value)
            if max_value - start == index - start:
                chunks += 1
                start = index + 1
        return chunks