class Solution:
    def solution_45_4(self, s: str) -> int:
        n = len(s)
        p_start = [[] for _ in range(n)]

        # odd palindromes
        for i in range(n):
            j = 0
            while i + j < n and i - j >= 0:
                if s[i + j] == s[i - j]:
                    p_start[i + j].append(i - j)
                else:
                    break
                j += 1

        # even palindromes
        for i in range(n):
            j = 0
            while i + j < n and i - j - 1 >= 0:
                if s[i + j] == s[i - j - 1]:
                    p_start[i + j].append(i - j - 1)
                else:
                    break
                j += 1

        min_counts = [math.inf for _ in range(n)]
        for i in range(n):
            for j in p_start[i]:
                min_counts[i] = min(
                    min_counts[i], 1 + (min_counts[j - 1] if j > 0 else 0)
                )

        return min_counts[n - 1] - 1