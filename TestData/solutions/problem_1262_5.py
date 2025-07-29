class Solution:
    def solution_1262_5(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0 
        m, n = len(nums1), len(nums2)
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                res = max(res, j-i)
                j += 1
            else:
                i += 1
        
        
        return res