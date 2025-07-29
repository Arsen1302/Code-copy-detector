class Solution:
    def solution_1027_3(self, s: str) -> int:
        n = len(s)
        suffixes = [0] * n
        unique = set()
        for i in reversed(range(n)):
            unique.add(s[i])
            suffixes[i] = len(unique)

        counter = 0
        unique = set()
        for i in range(n - 1):
            unique.add(s[i])
            if len(unique) == suffixes[i+1]:
                counter += 1

        return counter