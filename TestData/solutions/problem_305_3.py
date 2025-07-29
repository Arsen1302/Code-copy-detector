class Solution:
    def solution_305_3(self, word: str) -> bool:
        if word==word.lower() or word==word.upper() or word==(word[0].upper() + word[1:].lower()):
            return True
        return False