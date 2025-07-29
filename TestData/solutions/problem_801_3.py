class Solution:
    def solution_801_3(self, position: List[int]) -> int:
        return min(len(list(filter(lambda x: x%2 == 0, position))), len(list(filter(lambda x: x%2 == 1, position))))