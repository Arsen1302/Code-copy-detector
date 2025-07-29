class Solution:
    def solution_305_4(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()