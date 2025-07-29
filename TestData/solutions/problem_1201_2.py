class Solution:
    def solution_1201_2(self, word1: str, word2: str) -> str:
        ans = []
        for x, y in zip_longest(word1, word2, fillvalue=""):
            ans.append(x)
            ans.append(y)
        return "".join(ans)