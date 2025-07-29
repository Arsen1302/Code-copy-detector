class Solution:
    def solution_910_3(self, s: str) -> int:
        d = {0: -1}
        ans = cur = 0
        vowel = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        for i, c in enumerate(s):
            if c in vowel:
                cur ^= 1 << vowel[c]
            if cur not in d:
                d[cur] = i
            ans = max(ans, i - d[cur]) 
        return ans