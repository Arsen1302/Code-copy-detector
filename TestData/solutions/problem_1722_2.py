class Solution:
    def solution_1722_2(self, nums: List[int]) -> int:
        count = 0
        prev, nxt = 0, len(nums)
        for _, frequency in Counter(nums).items():
            nxt -= frequency
            count += prev * frequency * nxt
            prev += frequency
        return count