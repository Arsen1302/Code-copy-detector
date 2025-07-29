class Solution:
    def solution_1343_5(self, patterns: List[str], word: str) -> int:
        return sum(i in word for i in patterns)
        ```