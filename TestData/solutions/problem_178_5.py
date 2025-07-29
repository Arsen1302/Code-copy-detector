class Solution:
    def solution_178_5(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1, d2 = Counter(nums1), Counter(nums2)
        return [num for num in d1 &amp; d2 for count in range(min(d1[num], d2[num]))]