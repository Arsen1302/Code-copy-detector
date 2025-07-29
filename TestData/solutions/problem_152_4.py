class Solution:
    def solution_152_4(self, n: int, primes: List[int]) -> int:
        h, cnt, last, seen = [1], 0, -1, set()
        max_seen = -1

        while cnt < n:
            c = heappop(h)
            cnt += 1
            seen.add(c)
            for p in primes:
                if c * p not in seen and (len(h) <= n - cnt or c*p < max_seen):
                    heappush(h, c*p)
                    seen.add(c*p)
                    max_seen = max(max_seen, c*p)
            last = c
        return last