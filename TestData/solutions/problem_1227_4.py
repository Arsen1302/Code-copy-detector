class Solution:
    def solution_1227_4(self, word: str) -> int:
        return len(set(map(int, re.findall('\d+', word))))