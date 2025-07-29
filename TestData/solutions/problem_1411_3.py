class Solution:
    def solution_1411_3(self, word: str) -> int:
        return sum(set(word[i:j+1]) == set('aeiou') for i in range(len(word)) for j in range(i+1, len(word)))