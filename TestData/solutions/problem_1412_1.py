class Solution:
    def solution_1412_1(self, word: str) -> int:
        count = 0
        sz = len(word)
        
        for pos in range(sz):
            if word[pos] in 'aeiou':
                count += (sz - pos) * (pos + 1)
        
        return count