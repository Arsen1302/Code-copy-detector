class Solution:
    def solution_177_3(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        d = {}
        if len(nums1) > len(nums2):
            nums1,nums2=nums2,nums1
        for i in nums1:
            d[i] = 0
        
    
        for i in nums2:
            if i not in d:
                continue
            else:
                d[i] = d[i]+1
            
        res = []
        for k,v in d.items():
            if v > 0:
                res.append(k)
        return res