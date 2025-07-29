class Solution:
    def solution_1663_3(self, nums: List[int]) -> int:
        freq = Counter(x for x in nums if x&amp;1 == 0)
        return min(freq, key=lambda x: (-freq[x], x), default=-1)