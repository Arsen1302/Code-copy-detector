class Solution:
    def solution_1030_1(self, target: str) -> int:
        return len(list(groupby("0" + target)))-1