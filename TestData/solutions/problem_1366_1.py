class Solution:
    def solution_1366_1(self, word: str, ch: str) -> str:
        try:
            ix = word.index(ch)
            return word[:ix+1][::-1] + word[ix+1:]
        except ValueError:
            return word