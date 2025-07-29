class Solution:
    def solution_1343_1(self, patterns: List[str], word: str) -> int:
        return sum(x in word for x in patterns)