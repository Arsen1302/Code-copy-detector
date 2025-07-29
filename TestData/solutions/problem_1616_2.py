class Solution:
    def solution_1616_2(self, n: int, maxValue: int) -> int:
        MOD = 10 ** 9 + 7
        ans = maxValue
        freq = {x: 1 for x in range(1, maxValue + 1)}
        for k in range(1, n):
            if not freq:
                break
            nxt = collections.defaultdict(int)
            for x in freq:
                for m in range(2, maxValue // x + 1):
                    ans += math.comb(n - 1, k) * freq[x]
                    nxt[m * x] += freq[x]
            freq = nxt
            ans %= MOD
        return ans