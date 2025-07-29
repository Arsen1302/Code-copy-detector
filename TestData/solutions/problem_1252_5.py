class Solution:
    def solution_1252_5(self, s: str) -> int:
        i,j,x = 0,0,0
        while j < len(s):
            if s[j] in ['a', 'e', 'i', 'o', 'u'] and (s[j-1] <= s[j] or j == 0):
                j += 1
            else:
                if len(set(s[i:j])) == 5:
                    x = max(x,j-i)
                i = j
                j += 1
        if len(set(s[i:j])) == 5:
            x = max(x,j-i)
        return x