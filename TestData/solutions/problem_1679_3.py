class Solution:
    def solution_1679_3(self, word: str) -> bool:
        for i in range(len(word)):
            z=word[:i]+word[i+1:]
            if len(set(Counter(z).values()))==1:
                return True
        return False