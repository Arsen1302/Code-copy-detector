class Solution:
    def solution_607_3(self, name: str, typed: str) -> bool:
        i, j, m, n = 0, 0, len(name), len(typed)
        if n < m: return False
        while i < m and j < n:
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif j == 0 or typed[j] != typed[j - 1]: return False
            else:
                j += 1
        return i == m and typed[j:] == typed[j - 1] * (n - j)