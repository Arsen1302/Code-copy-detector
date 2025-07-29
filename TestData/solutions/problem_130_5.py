class Solution:
    def solution_130_5(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        return [x for x in freq if freq[x] == 1]