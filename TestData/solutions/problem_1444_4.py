class Solution:
    def solution_1444_4(self, words: List[str]) -> str:
        return next((word for word in words if word == word[::-1]), "")