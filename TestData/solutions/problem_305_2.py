class Solution:
    def solution_305_2(self, word: str) -> bool:
        if word.isupper(): return True
        if word.islower(): return True
        if word[0].isupper() and word[1:].islower(): return True
        return False