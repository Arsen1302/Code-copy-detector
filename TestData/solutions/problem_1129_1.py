class Solution:
    def solution_1129_1(self, accounts: List[List[int]]) -> int:
        return max([sum(acc) for acc in accounts])