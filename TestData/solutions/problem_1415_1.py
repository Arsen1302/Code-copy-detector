class Solution:
    def solution_1415_1(self, word1: str, word2: str) -> bool:
        freq = [0]*26
        for x in word1: freq[ord(x)-97] += 1
        for x in word2: freq[ord(x)-97] -= 1
        return all(abs(x) <= 3 for x in freq)