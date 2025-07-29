class Solution:
    def solution_801_4(self, position: List[int]) -> int:
        return min(len([1 for x in position if x%2 == 0]), len([1 for x in position if x%2 == 1]))