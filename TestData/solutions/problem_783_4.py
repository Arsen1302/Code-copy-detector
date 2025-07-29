class Solution:
    def solution_783_4(self, s: str, queries: List[List[int]]) -> List[bool]:
        len_s = len(s)
        freq = [defaultdict(int)] * len_s
        freq[0][s[0]] += 1
        for i in range(1, len_s):
            freq[i] = freq[i - 1].copy()
            freq[i][s[i]] += 1
        ans = [True] * len(queries)
        for i, (left, right, k) in enumerate(queries):
            left1 = left - 1
            n_odd = sum((n - (freq[left1][c] if left1 > -1 else 0)) % 2
                        for c, n in freq[right].items())
            ans[i] = n_odd - 2 * k <= 1
        return ans