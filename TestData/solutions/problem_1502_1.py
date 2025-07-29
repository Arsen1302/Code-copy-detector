class Solution:
    def solution_1502_1(self, words: List[str], pref: str) -> int:
        return sum(word.find(pref) == 0 for word in words)