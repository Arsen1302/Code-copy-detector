class Solution:
    def solution_1679_4_1(self, c):
        c = Counter(c)
        return len(list(set(list(c.values())))) == 1

    def solution_1679_4_2(self, word: str) -> bool:
        for i in range(len(word)):
            if self.solution_1679_4_1(word[:i] + word[i + 1:]):
                return True
        return False