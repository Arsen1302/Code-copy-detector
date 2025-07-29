class Solution:
    def solution_1529_2(self, start: int, goal: int) -> int:
        return bin(start ^ goal).count("1")