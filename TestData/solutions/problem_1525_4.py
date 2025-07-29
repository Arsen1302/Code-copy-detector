class Solution:
    def solution_1525_4(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        p=[[],[]]
        for i in set(nums1):
            if i in nums2:
                continue
            else:
                p[0].append(i)
        for i in set(nums2):
            if i in nums1:
                continue
            else:
                p[1].append(i)
        return p