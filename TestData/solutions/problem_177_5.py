class Solution:
    def solution_177_5(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) &amp; set(nums2))