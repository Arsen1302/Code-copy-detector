class Solution:
    def solution_178_4(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1, dict2 = Counter(nums1), Counter(nums2)
        res = []
        for key in dict1:
            if key in dict1 and key in dict2:
                res += [key] * min(dict1[key], dict2[key])
        return res