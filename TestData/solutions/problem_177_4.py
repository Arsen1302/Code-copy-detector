class Solution:
    def solution_177_4(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [] # list 1, for saving same elem of num1 and num2.
        fres = [] # list 2, for converting set to list.
        for i in range(len(nums1)): # read elem from nums1
            for j in range(len(nums2)): # read elem from nums2
                if nums1[i] == nums2[j]: # identical elements of both list.
                    res.append(nums1[i]) # appending identical elements in list 1.
        
        fres = set(res) # using set to remove duplicate elements &amp; typecasting it back to list.
        
        return fres