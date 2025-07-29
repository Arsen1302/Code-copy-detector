class Solution:
    def solution_1626_1_1(self, nums: List[int], k: int) -> int:
        hamming = sorted([self.solution_1626_1_2(num) for num in set(nums)])
        ans = 0
        for h in hamming:
            ans += len(hamming) - bisect.bisect_left(hamming, k - h)
        return ans
        
    def solution_1626_1_2(self, n):
        ans = 0
        while n:
            n &amp;= (n - 1)
            ans += 1
        return ans