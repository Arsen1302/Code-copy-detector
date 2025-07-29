class Solution:
    def solution_333_4(self, nums: List[int], k: int) -> int:
        sums = defaultdict(int)
        curr = res = 0
        sums[0] = 1
        for num in nums:
            curr += num
            res += sums[curr - k]
            sums[curr] += 1
        return res