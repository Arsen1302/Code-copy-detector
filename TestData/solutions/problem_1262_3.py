class Solution:
    def solution_1262_3(self, nums1: List[int], nums2: List[int]) -> int:
        ans = ii = 0 
        for i, x in enumerate(nums2): 
            while ii <= i and ii < len(nums1) and nums1[ii] > nums2[i]: ii += 1
            if ii < len(nums1) and nums1[ii] <= nums2[i]: ans = max(ans, i - ii)
        return ans