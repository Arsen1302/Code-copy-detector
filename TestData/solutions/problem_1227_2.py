class Solution:
    def solution_1227_2(self, word: str) -> int:
        seen = set()
        for key, grp in groupby(word, str.isdigit): 
            if key: seen.add(int("".join(grp)))
        return len(seen)