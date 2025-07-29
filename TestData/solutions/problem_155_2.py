class Solution:
    def solution_155_2(self, words: List[str]) -> int:
         return max([len(s1) * len(s2) for s1, s2 in combinations(words, 2)  if not (set(s1) &amp; set(s2))], default=0)