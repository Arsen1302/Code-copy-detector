class Solution:
    def solution_1553_3(self, words: List[str], s: str) -> int:
        return sum([1 for w in words if w == s[:len(w)]])