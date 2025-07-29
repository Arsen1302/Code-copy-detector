class Solution:
    def solution_1425_5(self, words1: List[str], words2: List[str]) -> int:
        fix = lambda w: set(filter(lambda x: x[1] == 1, Counter(w).items()))

        return len(fix(words1) &amp; fix(words2))