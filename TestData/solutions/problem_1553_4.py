class Solution:
    def solution_1553_4(self, words: List[str], s: str) -> int:
        return sum(w == s[:len(w)] for w in words)