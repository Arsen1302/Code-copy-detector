class Solution:
    def solution_1680_5(self, nums1: List[int], nums2: List[int]) -> int:
        
        res_a = 0
        res_b = 0


        for j in nums2:
            res_b^=j

        for i in nums1:
            res_a^=i

        if len(nums2) %2 ==0 :
            if len(nums1) %2 == 0 :
                return 0 
            return res_b 

        else :
            if len(nums1) %2 == 0 :
                return res_a
            return res_a ^ res_b