class Solution:
    def solution_1129_4(self, accounts: List[List[int]]) -> int:
        return max([sum(i) for i in accounts])