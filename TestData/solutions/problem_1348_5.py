class Solution:
    # 1 liner
    # 3 parts. 1. starting from 'a' to word[0]
    # 2. move from each word[i] to word[i+1]
    # 3. add len(word) for len(word) key-presses

    def solution_1348_5(self, word: str) -> int:
        return min(abs(ord('a') - ord(word[0])), 26 - abs(ord('a') - ord(word[0]))) + sum(min(abs(ord(word[i]) - ord(word[i+1])), 26 - abs(ord(word[i]) - ord(word[i+1]))) for i in range(len(word)-1)) + len(word)

    # O(n) time : O(1) space
    def solution_1348_5(self, word: str) -> int:
        prev, res = 'a', len(word)
        for c in word:
            dist = abs(ord(prev) - ord(c))
            res += min(dist, 26 - dist)
            prev = c
        return res