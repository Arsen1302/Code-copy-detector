class Solution:
    def solution_1525_3(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        x = [i for i in nums1 if i not in nums2];
        y = [j for j in nums2 if j not in nums1];
        return [list(set(x)) , list(set(y))];