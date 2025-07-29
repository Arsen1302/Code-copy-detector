class Solution:
    def solution_1525_5(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s = set(nums1)
        s1 = set(nums2)
        return [list(s-s1),list(s1-s)]