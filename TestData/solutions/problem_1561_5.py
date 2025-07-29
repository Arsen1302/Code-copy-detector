class Solution:
    def solution_1561_5(self, num: str) -> str:
        return next((x*3 for x in "9876543210" if x*3 in num), "")