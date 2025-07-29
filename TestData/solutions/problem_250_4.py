class Solution:
    def solution_250_4(self, s: str) -> str:
        return "".join([letter * frequency for letter, frequency in sorted(collections.Counter(s).items(), key = lambda x: x[1], reverse = True)])