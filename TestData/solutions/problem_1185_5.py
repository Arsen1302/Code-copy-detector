class Solution:
    def solution_1185_5(self, nums: List[int]) -> int:
        freq = {}
        for x in nums: freq[x] = 1 + freq.get(x, 0)
        return sum(x for x in nums if freq[x] == 1)