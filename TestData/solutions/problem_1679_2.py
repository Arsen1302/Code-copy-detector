class Solution:
    def solution_1679_2(self, word: str) -> bool:
        return any(len(set(Counter(word[:i]+word[i+1:]).values()))==1 for i in range(len(word)))