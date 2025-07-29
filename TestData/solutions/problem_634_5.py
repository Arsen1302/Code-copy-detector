class Solution:
    def solution_634_5(self, words: List[str], order: str) -> bool:
        return sorted(words, key=lambda word: [order.index(c) for c in word]) == words