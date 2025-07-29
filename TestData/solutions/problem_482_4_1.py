class Solution:
    def solution_482_4_1(self, s: str, words: List[str]) -> int:
        def solution_482_4_2(x, y):
            it = iter(y)
            return all(c in it for c in x)
        c=0
        wordsset = set(words)
        for i in wordsset:
            if solution_482_4_2(i,s):
                c = c+words.count(i)
        return c