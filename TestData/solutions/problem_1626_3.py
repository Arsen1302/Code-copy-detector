class Solution:
    def solution_1626_3(self, nums: List[int], k: int) -> int:
        hamming = Counter([num.bit_count() for num in set(nums)])
        ans = 0
        for h1 in hamming:
            for h2 in hamming:
                if h1 + h2 < k:
                    continue
                ans += hamming[h1] * hamming[h2]
        return ans