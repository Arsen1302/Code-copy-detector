class Solution:
    def solution_1201_3(self, word1: str, word2: str) -> str:
        return "".join(x+y for x, y in zip_longest(word1, word2, fillvalue=""))