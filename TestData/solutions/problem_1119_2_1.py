class Solution:
    def solution_1119_2_1(self, word1: str, word2: str) -> bool:
        
        def solution_1119_2_2(word):
            """Return freq table of word."""
            freq = {}
            for c in word: freq[c] = 1 + freq.get(c, 0)
            return freq
        
        freq1, freq2 = solution_1119_2_2(word1), solution_1119_2_2(word2)
        return freq1.keys() == freq2.keys() and sorted(freq1.values()) == sorted(freq2.values())