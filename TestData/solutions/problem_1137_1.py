class Solution:
    def solution_1137_1(self, allowed: str, words: List[str]) -> int:
        return sum(set(allowed) >= set(i) for i in words)