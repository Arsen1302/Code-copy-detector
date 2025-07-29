class Solution:
    def solution_1053_5(self, n: int, rounds: List[int]) -> List[int]:
        
        start, end = rounds[0], rounds[-1]
        
        if start <= end:
            return range(start, end + 1)
        else:
            return list(range(1, end + 1)) + list(range(start, n + 1))