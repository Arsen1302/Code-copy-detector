class Solution:
    def solution_1389_4(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        set3 = set(nums3)
        set12 = set1.intersection(set2)
        set23 = set2.intersection(set3)
        set13 = set1.intersection(set3)
        
        return (set12.union(set23)).union(set13)