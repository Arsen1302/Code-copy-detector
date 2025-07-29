class Solution:
    def solution_197_4(self, n: int) -> List[int]:
        return sorted(range(1, n+1), key=str)