class Solution:
    def solution_266_3(self, words: List[str]) -> List[str]:
        s, m = set(words), {}
        dp = lambda w: m[w] if w in m else any(w[:i] in s and (w[i:] in s or dp(w[i:])) for i in range(1, len(w)))
        return filter(dp, words)