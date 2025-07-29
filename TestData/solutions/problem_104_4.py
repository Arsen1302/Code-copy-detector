class Solution:
    def solution_104_4(self, nums: List[int]) -> bool:
        return set(collections.Counter(nums).values()) != set([1])