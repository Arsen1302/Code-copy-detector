class Solution:
    def solution_1343_3(self, patterns: List[str], word: str) -> int:
        return len([pattern for pattern in patterns if pattern in word])