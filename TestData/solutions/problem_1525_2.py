class Solution:
    def solution_1525_2(self, n1: List[int], n2: List[int]) -> List[List[int]]:
        return [set(n1) - set(n2),set(n2) - set(n1)]