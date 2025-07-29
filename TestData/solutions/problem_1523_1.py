class Solution:
    def solution_1523_1(self, directions: str) -> int:
        return sum(d!='S' for d in directions.lstrip('L').rstrip('R'))