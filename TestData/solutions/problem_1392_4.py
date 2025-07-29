class Solution:
    def solution_1392_4(self, seats: List[int], students: List[int]) -> int:
        return sum(abs(x-y) for x, y in zip(sorted(seats), sorted(students)))