class Solution:
    def solution_1233_5(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for n in nums:
            freq[n - int("".join(str(n)[::-1]))] += 1
        return (sum((n - 1) * n // 2 for n in freq.values() if n > 1) %
                1_000_000_007)